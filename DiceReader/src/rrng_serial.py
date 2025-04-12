import serial
import time

def rodar_dado():
    iniciar_serial()
    ser.write('RODAR_DADO;'.encode('ascii'))
    encerrar_serial()

def iniciar_serial():
    global ser
    ser = serial.Serial('COM4', 9600)
    time.sleep(2)

def encerrar_serial():
    time.sleep(2)
    ser.close()