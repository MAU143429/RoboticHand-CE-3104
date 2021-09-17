from Hardware.Robotic_Hand.Translator import Translator

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

        print("SE HA REGISTRADO EL DELAY CON DURACION DE " + str(self.value) + " " + str(self.unit) +  " EN LA LINEA " + str(self.line))
        t = Translator()
        t.Create_Delay(self.value,self.unit)

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

class Move:
    def __init__(self, finger, movement, line):
        self.finger = finger
        self.movement = movement
        self.line = line
        print("SE HA REGISTRADO EL METODO MOVE CON MOVIMIENTO " + str(self.movement) + " EN EL DEDO " + str(self.finger) + " EN LA LINEA " + str(self.line))
