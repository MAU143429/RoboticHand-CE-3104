import serial
import time

serial_port = serial.Serial('COM5',9600)
time.sleep(2)

f = open('Pruebas\song.txt', 'r')

for line in f:
    cad = 'mov,T;true/'
    serial_port.write(cad.encode())
    time.sleep(1)
    result = serial_port.readline().decode()
    print("MENSAJE DE LA PLACA---->" + result + "*********")

serial_port.close()

