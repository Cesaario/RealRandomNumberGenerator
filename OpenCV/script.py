import rrng_serial as serial
import rrng_cv as cv
import time

def rodar_dado_ler_face():
    pass

serial.iniciar_serial()
serial.rodar_dado()
serial.encerrar_serial()

print("capturando")
cv.iniciar_captura()
print("face", cv.obter_face_ate_sucesso())
cv.encerrar_captura()