
class Let:
    def __init__(self, id, value, line):
        self.id = id
        self.value = value
        self.line = line
        print("SE HA REGISTRADO EL LET  " + self.id + " CON EL VALOR DE " + str(self.value) + " EN LA LINEA " + str(self.line))

class Del:
    def __init__(self, value, line):
        self.value = value
        self.line = line
        print("SE HA REGISTRADO EL DELAY CON DURACION DE " + str(self.value) + " EN LA LINEA " + str(self.line))


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