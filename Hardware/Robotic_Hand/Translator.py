import serial
import time
import os

class Translator:

    def __init__(self):
        print("LOAD INFO....")


    def Read(self,num):
        msg = []
        with open('../../Software/Lexical_Analysis/test.txt') as f:
            msg = f.readlines()
        if num >= len(msg):
            return " "
        else:
            return msg[num]

    def ReadAll(self):
        with open('../../Software/Lexical_Analysis/test.txt','r') as f:
            msgfull = f.read()
            return msgfull

    def Write(self, data):
        ReadData = Translator().ReadAll()
        file = open('../../Software/Lexical_Analysis/test.txt','w')
        note = data + "\n" + ReadData
        file.write(note)
        print("LINE TRANSLATED")
        file.close()


    def Clean(self):
        file = open('../../Software/Lexical_Analysis/test.txt', 'wb')
        clean_data = ""
        file.write(clean_data.encode())
        print("CLEANING....")
        file.close()

    def Create_Delay(self, time,unit):
        result1 = ("del," + str(time) + ";" + str(unit) + "/")
        t = Translator()
        t.Write(result1)

    def Create_Move(self, finger, status):
        result2 = ("mov," + str(finger) + ";" + str(status) + "/")
        t = Translator()
        t.Write(result2)

class Execute:

    def __init__(self):
        print("EXECUTING PROGRAM....")
    '''
    PRETENDE QUE EXISTA UN SLEEP CADA VEZ QUE LEE UN DELAY
    '''
    def Create_delays(self,timer, unit):

      time = int(timer)
      if unit == "Mil":
        mil = (time/10000)
        time.sleep(mil)
      elif unit == "Min":
        min = (time/1000)
        time.sleep(min)
      else:
        seg = time
        time.sleep(seg)

    '''
    
    ENVIA POR EL PUERTO COM A LA PLACA LO QUE SE ENCUENTRA EN 
    
    '''
    def execute(self):
        print("ABRIENDO PUERTO SERIAL")
        serial_port = serial.Serial('COM5',9600,timeout = 1)
        time.sleep(2)
        print("PUERTO SERIAL ABIERTO")
        send = []
        print("LEYENDO ARCHIVO TEST.TXT")
        with open('../../Software/Lexical_Analysis/test.txt','r') as f:
            send = f.readlines()
            print("DENTRO DEL WITH")
            print(send)
            print(len(send))
        print("ARCHIVO LEIDO Y ALMACENADO ")
        print("ESTA ES LA INFORMACION QUE VOY A ENVIAR A LA PLACA ----->  ")
        numline = 0
        while(numline < len(send)):
            cad = send[numline]
            if(cad != " "):
                step1 = cad.find(',')
                step2 = cad.find(';')
                step3 = cad.find('/')
                action = cad[0:step1]
                print("MENSAJE HACIA LA PLACA---->" + cad + "*********")
                if action == "del":
                    #timer = cad[step1+1:step2]
                    #unit = cad[step2+1:step3]
                    serial_port.write(cad.encode())
                    print("MENSAJE DELAY ENVIADO A LA PLACA SATISFACTORIAMENTE")
                    time.sleep(1)
                    #self.Create_delays(timer, unit)
                    result = serial_port.readline().decode('ascii')
                    print("MENSAJE DE LA PLACA---->" + result + "*********")
                    numline += 1
                    print("ENVIO FINALIZADO")
                else:
                    serial_port.write(cad.encode())
                    print("MENSAJE MOVE ENVIADO A LA PLACA SATISFACTORIAMENTE")
                    time.sleep(1)
                    result = serial_port.readline().decode('ascii')
                    print("MENSAJE DE LA PLACA---->" + result + "*********")
                    numline += 1
                    print("ENVIO FINALIZADO")
            else:
                numline += 1

