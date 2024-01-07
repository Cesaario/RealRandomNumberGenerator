import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

threshold = 200

def obter_frame():
    global threshold
    print(threshold)
    _, frame = cap.read()

    blur = cv.blur(frame, (4,4))
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY) 
    bw = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)[1]

    return frame, bw

# def obter_circulos(imagem):
#     circulos = cv.HoughCircles(imagem,  
#                    cv.HOUGH_GRADIENT, dp=1, minDist=12, param1 = 50, 
#                param2 = 8, minRadius = 1, maxRadius = 30)
    
#     return circulos[0] if circulos is not None else None

#detector = cv.SimpleBlobDetector_create()
#blobs = detector.detect(imagem)

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

# def teste_circulos(imagem):
#     blur = cv.blur(imagem, (4,4))
#     gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY) 
#     bw = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)[1]

#     contours, hierarchy = cv.findContours(bw,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

#     circulos = []

#     for cnt in contours:
#         (x,y),radius = cv.minEnclosingCircle(cnt)
#         if cv.isContourConvex(cnt) or radius < 1:
#             continue
#         center = (int(x),int(y))
#         radius = int(radius)
#         circulos.append([int(x), int(y), int(radius)])
#         cv.circle(imagem,center,radius,(0,255,0),2)

#     print("---")
#     print(circulos)

def desenhar_circulos(imagem, circulos):
    if circulos is not None:
        circulos = np.uint16(np.around(circulos))
        for i in circulos:
            # draw the outer circle
            cv.circle(imagem,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(imagem,(i[0],i[1]),2,(255,0,0),10)

def desenhar_face_dado(imagem, circulos):
    if circulos is None:
        return

    face_dado = len(circulos)

    coords_x = [item[0] for item in circulos]
    coords_y = [item[1] for item in circulos]

    media_x = sum(coords_x) / len(coords_x)
    media_y = sum(coords_y) / len(coords_y)

    cv.circle(imagem, (int(media_x),int(media_y)), 25, (0,255,0), 2)
    cv.putText(imagem, str(face_dado), (int(media_x) + 30, int(media_y) + 30), cv.FONT_HERSHEY_SIMPLEX,  
                   1, (0,255,0), 2, cv.LINE_AA) 

def executar_comandos():
    global threshold

    tecla = cv.waitKey(1)
    if tecla == ord('q'):
        return -1
    if tecla == ord('p'):
        threshold = threshold + 10
    if tecla == ord('o'):
        threshold = threshold - 10



while True:
    
    original, preto_branco = obter_frame()

    #teste_circulos(original)

    circulos = obter_circulos(preto_branco)

    desenhar_circulos(original, circulos)
    desenhar_face_dado(original, circulos)

    cv.imshow("Camera original", original) 
    cv.imshow("Camera preto e branco", preto_branco) 

    retorno_comando = executar_comandos()

    if retorno_comando == -1:
        break

cap.release()
cv.destroyAllWindows()