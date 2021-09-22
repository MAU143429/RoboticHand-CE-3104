from Hardware.Robotic_Hand.Translator import Translator
from Software.Semantic.reserved import *
from Software.Semantic.Generate_Error import *
from Software.Semantic.BooleanValue import *
class Let:
    def __init__(self, id, value,line,symbol_table,result):
        self.id = id
        self.value = value  # Let num = var1;   # Let num = True;
        self.line = line
        self.table = symbol_table
        self.exist_var = result
        print("SE HA REGISTRADO EL LET  " + self.id + " CON EL VALOR DE " + str(self.value) + " EN LA LINEA " + str(self.line))

        '''
        EXISTANCE ANALYSIS
        '''
        if self.exist_var:
            found = False
            for var in self.table:  
                if var == str(value):
                    if (self.table[self.value]["type"]) != (self.table[self.id]["type"]):
                        errorHandler = Generate_Error(4, self.line)
                        errorHandler.Execute()
                        found = True
                    else:
                        self.table[self.id]["value"] = self.table[self.value]["value"]
                        found = True
                        print("SE HA REGISTRADO EL LET  " + self.id + " CON EL VALOR DE " + str(self.value) + " EN LA LINEA " + str(self.line))
                        break

            if not found:
                errorHandler = Generate_Error(5, self.line)
                errorHandler.Execute()


class Del:
    def __init__(self, value, unit ,table, line):
        self.value = value
        self.unit = unit
        self.line = line
        self.table = table
        self.checker = MoveDelayCheck(self.unit)
        if self.checker.check_units():
            print("SE HA REGISTRADO EL DELAY CON DURACION DE " + str(self.value) + " " + self.unit +  " EN LA LINEA " + str(self.line))
            t = Translator()
            t.Create_Delay(self.value,self.unit)
        else:
            e_msg = "SYNTAX ERROR AT LINE " + str(self.line) + ". INVALID TIME SUFFIX"
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
    def __init__(self, finger, movement,symbol_table, line):
        self.finger = finger
        self.movement = movement
        self.final_movement = None
        self.line = line
        self.table = symbol_table
        self.checker = MoveDelayCheck(self.finger)

        '''
        MOVEMENT ANALYSIS
        '''
        if isinstance(validate_real_bool(movement), bool):
            self.final_movement = validate_bool(movement)
        else:
            for var in self.table:
                if var == movement:
                    if isinstance(validate_real_bool(self.table[self.movement]["value"]),bool):
                        self.final_movement = self.table[self.movement]["value"]
                        print("EL VALOR DE FINAL MOVEMENT COMO ---> " + self.final_movement)
                        break
                    else:
                        errorHandler = Generate_Error(12, self.line)
                        errorHandler.Execute()

            if self.final_movement == None:
                errorHandler = Generate_Error(5, self.line)
                errorHandler.Execute()
        '''
        FINGER ANALYSIS
        '''
        if isinstance(finger, list): # SI INGRESA UNA LISTA DE DEDOS
            if self.checker.check_fingers():
                t = Translator()
                cont = 0
                while(cont < len(finger)):
                    t.Create_Move(finger[cont], self.final_movement)
                    cont += 1
            else:
                errorHandler = Generate_Error(11, self.line)
                errorHandler.Execute()

        elif self.checker.check_fingers(): # SI NO ES LISTA
            print("SE HA REGISTRADO EL METODO MOVE CON MOVIMIENTO " + str(self.final_movement) + " EN EL DEDO " + str(self.finger) + " EN LA LINEA " + str(self.line))
            t = Translator()
            t.Create_Move(self.finger,self.final_movement)
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
