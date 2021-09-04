import serial
import time

class Translator:

    def __init__(self):
        print("init")

    def Read(self,num):
        msg = []
        with open('Instructions.txt') as f:
            msg = f.readlines()

        if num >= len(msg):
            return " "
        else:
            return msg[num]

    def ReadAll(self):
        with open('Execute.txt') as f:
            msgfull = f.read()
        return msgfull

    def Write(self, data):
        ReadData = Translator().ReadAll()
        file = open('Execute.txt', 'wb')
        data = ReadData + data
        file.write(data.encode())
        file.close()

    def Clean(self):
        file = open('Execute.txt', 'wb')
        clean_data = ""
        file.write(clean_data.encode())
        file.close()

    def Create_String(self,txt):
        action_key = txt[0]
        if action_key == 'D':
            step1 = txt.find(',')
            step2 = txt.find(')')
            time = txt[6:step1]
            unit = txt[step1+2:step2-1]
            result1 = ("del,"+ time + ";" + unit + "/")
            if result1 == "del,;/":
                return " "
            else:
                return result1

        else:
            step1 = txt.find(',')
            step2 = txt.find(')')
            finger = txt[6:step1-1]
            status = txt[step1 + 2:step2 - 1]
            result2 = ("mov," + finger + ";" + status + "/")
            if result2 == "mov,;/":
                return " "
            else:
                return result2


def Translate():
    p = Translator()
    p.Clean()
    numline = 0
    line = "********* FIRST LINE ***********"
    while (line != " "):
        line = p.Read(numline)
        script = p.Create_String(line)
        print(script + "\n" );
        p.Write(script + "\n")
        numline += 1

def Create_delays(timer, unit):

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



exe = Translate()
time.sleep(3)
serial_port = serial.Serial('COM5',115200,timeout = 1)
time.sleep(2)
send = []
with open('Execute.txt') as f:
    send = f.readlines()
numline = 0
line = "********* FIRST LINE ***********"
while (line != " "):
    cad = send[numline]
    step1 = cad.find(',')
    step2 = cad.find(';')
    step3 = cad.find('/')
    action = cad[0:step1]
    print("MENSAJE HACIA LA PLACA---->" + cad + "*********")
    if action == "del":
        timer = cad[step1+1:step2]
        unit = cad[step2+1:step3]
        serial_port.write(cad.encode())
        Create_delays(timer,unit)
        result = serial_port.readline().decode()
        print("MENSAJE DE LA PLACA---->" + result + "*********")
        numline += 1
    else:
        serial_port.write(cad.encode())
        time.sleep(500)
        result = serial_port.readline().decode()
        print("MENSAJE DE LA PLACA---->" + result + "*********")
        numline += 1