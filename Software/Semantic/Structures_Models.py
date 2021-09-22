from Hardware.Robotic_Hand.Translator import Translator
from Software.Semantic.reserved import *
from Software.Semantic.Generate_Error import *
class Let:
    def __init__(self, id, value, line):
        self.id = id
        self.value = value  # Let num = 42;   # Let num = True;
        self.line = line
        print("SE HA REGISTRADO EL LET  " + self.id + " CON EL VALOR DE " + str(self.value) + " EN LA LINEA " + str(self.line))

class Del:
    def __init__(self, value, unit , line):
        self.value = value
        self.unit = unit
        self.line = line

        self.checker = MoveDelayCheck(self.unit)
        if self.checker.check():
            print("SE HA REGISTRADO EL DELAY CON DURACION DE " + str(self.value) + " " + self.unit +  " EN LA LINEA " + str(self.line))
            t = Translator()
            t.Create_Delay(self.value,self.unit)
        else:
            e_msg = "SYNTAX ERROR AT LINE " + str(self.line) + ". INVALID TIME SUFFIX"
            #print(e_msg)
            errorHandler = Generate_Error(9, self.line)
            errorHandler.Execute()

class Print:
    def __init__(self, value, line):
        self.value = value
        self.line = line
        print("SE IMPRIMIRA EN LA CONSOLA -->  " + str(self.value) + " EN LA LINEA " + str(self.line))

class Opera:
    def __init__(self, operator, operand, operand2, line):
        self.operator = operator
        self.operand = operand
        self.operand2 = operand2
        self.line = line

    def Operate(self):
        result = None
        if not isinstance(self.operand, int) and isinstance(self.operand2, int):
            result = (self.operator, self.operand, self.operand2)
        else:
            if self.operator == "+":
                result = self.operand + self.operand2
            elif self.operator == "-":
                result = self.operand - self.operand2
            elif self.operator == "/":
                result = self.operand / self.operand2
            elif self.operator == "**":
                result = self.operand ** self.operand2
            elif self.operator == "*":
                result = self.operand * self.operand2
        print("SE DETECTO UN OPERA DE FORMA (" + str(self.operator) + "," + str(self.operand) + ","+ str(self.operand2) + ")" + " CON RESULTADO " + str(result) + " EN LA LINEA " + str(self.line))
        return result

class Loop:
    def __init__(self, line):
        self.line = line
        print("LOOP")

class For:
    def __init__(self, id, const1, range, const2, line):
        self.id = id
        self.const1 = const1
        self.range = range
        self.const2 = const2
        self.line = line
        print("FOR")

class While:
    def __init__(self, line):
        self.line = line
        print("WHILE")

class Move:
    def __init__(self, finger, movement, line):
        self.finger = finger
        self.movement = movement
        self.line = line
        self.checker = MoveDelayCheck(self.finger)
        if isinstance(finger, list):
            print("SOY UNA LISTA DE DEDOS: " + str(finger))
        elif self.checker.check():
            print("SE HA REGISTRADO EL METODO MOVE CON MOVIMIENTO " + str(self.movement) + " EN EL DEDO " + str(self.finger) + " EN LA LINEA " + str(self.line))
        else:
            errorHandler = Generate_Error(10, self.line)
            errorHandler.Execute()

class simpleListBuilder:
    def createList(self, fingers):
        simpleList = []
        for i in fingers:
            if isinstance(i, list):
                simpleList += self.createList(i)
            else:
                simpleList.append(i)
        return simpleList