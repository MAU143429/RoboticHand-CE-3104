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
    def __init__(self, value, line, myTable):
        self.value = value
        self.line = line
        self.table = myTable
        self.stringsList = myTable.getStringList()
        self.printLogger = ""
        self.printChecking()

        print("SE IMPRIMIRA EN LA CONSOLA -->  " + str(self.printLogger) + " DESDE LA LINEA " + str(self.line))

    def printChecking(self):

        for var in self.value:
            if var in self.stringsList:
                self.printLogger = self.printLogger + var[1:-1]
            else:
                self.printLogger = self.printLogger + str(self.table.getValue(var, self.line))




class If:
    def __init__(self, expression1, comparisonSymbol, expression2, symbol_table, line):
        self.expression1 = expression1
        self.comparisonSymbol = comparisonSymbol
        self.expression2 = expression2
        self.table = symbol_table
        self.line = line

    def Comparison(self):
        exist1 = True
        exist2 = True
        if not isinstance(validate_real_bool(self.expression1), bool) or isinstance(self.expression1, int):
            for var in self.table:
                if (var == self.expression1):
                    if self.table[var]["value"] != None:
                        self.expression1 = self.table[var]["value"]
                        exist1 = True
                        break
                    else:
                        exist1 = False
        if not isinstance(validate_real_bool(self.expression2), bool) or isinstance(self.expression2, int):
            for var in self.table:
                if (var == self.expression2):
                    if self.table[var]["value"] != None:
                        self.expression2 = self.table[var]["value"]
                        exist2 = True
                        break
                    else:
                        exist2 = False

        if exist1 and exist2:
            self.Operate(self.expression1, self.expression2)
        else:
            errorHandler = Generate_Error(5, self.line)
            errorHandler.Execute()

    def Operate(self, var1, var2):
        if isinstance(validate_real_bool(var1), bool) and isinstance(validate_real_bool(var2), bool):
            if (self.comparisonSymbol == "=="):
                if (var1 == var2):
                    print("true")
        elif isinstance(var1, int) and isinstance(var2, int):
            if (self.comparisonSymbol == "=="):
                if (var1 == var2):
                    print("true")
            elif (self.comparisonSymbol == ">="):
                if (var1 >= var2):
                    print("true")
            elif (self.comparisonSymbol == "<="):
                if (var1 <= var2):
                    print("true")
            elif (self.comparisonSymbol == ">"):
                if (var1 > var2):
                    print("true")
            else:
                if (var1 < var2):
                    print("true")
        else:
            errorHandler = Generate_Error(14, self.line)
            errorHandler.Execute()

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
    def __init__(self, finger, movement, symbol_table, line):
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

