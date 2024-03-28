import numpy as np
import cv2 as cv
import time

threshold = 60

def iniciar_captura():
    global cap
    cap = cv.VideoCapture(0)

def encerrar_captura():
    cap.release()

def obter_frame():
    global threshold
    _, frame = cap.read()

    blur = cv.blur(frame, (4,4))
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY) 
    bw = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)[1]

    return frame, bw

def obter_circulos(imagem):
    contours, _ = cv.findContours(imagem,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    circulos = []

    for cnt in contours:
        (x,y),radius = cv.minEnclosingCircle(cnt)
        if cv.isContourConvex(cnt) or radius < 2:
            continue
        center = (int(x),int(y))
        radius = int(radius)
        circulos.append([int(x), int(y), int(radius)])
        cv.circle(imagem,center,radius,(0,255,0),2)

    return circulos if len(circulos) > 0 else None

def obter_face():
    _, preto_branco = obter_frame()
    circulos = obter_circulos(preto_branco)
    
    return None if circulos == None else len(circulos)

# auxiliar para reduzir o impacto das instabilidades na leitura das faces
def obter_face_mais_frequente():
    faces = []
    for i in range(10):
        face = obter_face()
        if(face is not None):   
            faces.append(face)
    
    if(len(faces) == 0):
        return None

    unicos, contagem = np.unique(faces, return_counts=True)
    index = np.argmax(contagem)
    return unicos[index]

def obter_face_ate_sucesso():
    # tentar ler a imagem até ela parar para garantir que vai ser um dado válido
    tentativas = 0
    while(tentativas < 10):
        face = obter_face_mais_frequente()
        if face == None:
            print("sem face válida...")
            time.sleep(0.5)
            tentativas += 1
        else:
            return face
    return None

def obter_face_dado_com_captura():
    iniciar_captura()
    face = obter_face_ate_sucesso()
    encerrar_captura()

    return face
        

#iniciar_captura()
#print(obter_face_ate_sucesso())
#encerrar_captura()