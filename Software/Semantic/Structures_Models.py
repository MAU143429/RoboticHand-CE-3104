

class Let:
    def __init__(self, id, value, line):
        self.id = id
        self.value = value
        self.line = line
        print("SE HA REGISTRADO EL LET  " + self.id + " CON EL VALOR DE " + str(self.value) + " EN LA LINEA " + str(self.line))

class Del:
    def __init__(self, value, unit , line):
        self.value = value
        self.unit = unit
        self.line = line
        print("SE HA REGISTRADO EL DELAY CON DURACION DE " + str(self.value) + " " + str(self.unit) +  " EN LA LINEA " + str(self.line))

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
        print("SE DETECTO UN OPERA DE FORMA (" + str(self.operator) + "," + str(self.operand) + ","+ str(self.operand2) + ") EN LA LINEA " + str(self.line))
