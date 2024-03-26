import serial
import time

def rodar_dado():
    print("exec")
    ser.write('RODAR_DADO;'.encode('ascii'))

def iniciar_serial():
    global ser
    ser = serial.Serial('COM4', 9600)
    time.sleep(2)

def encerrar_serial():
    time.sleep(2)
    print("closing")
    ser.close()