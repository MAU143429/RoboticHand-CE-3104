from Hardware.Robotic_Hand.Translator import Translator
from Software.Semantic.reserved import *
from Software.Semantic.Generate_Error import *
from Software.Semantic.BooleanValue import *
from Software.SymbolsTable import *
myTable = SymbolsTable()
from Software.Print_Log import *


class Main():
    def __init__(self, instructions):
        self.instructions = instructions
        if self.instructions != None:
            for i in self.instructions:
                if i[0] == "MAIN":
                    if i[1] != None:
                        self.runCode(i[1])

    def runCode(self, functionInstructions):
        print(functionInstructions)
        if functionInstructions != None:
            for i in functionInstructions:
                if i[0] == "LET":
                    print("LET")
                    result = myTable.insertValue(i[2], i[1], i[3])
                    Let(i[1], i[2], i[3], myTable.table, result)
                elif i[0] == "MOVE":
                    print("MOVE")
                    Move(i[1], i[2], myTable.table, i[3])
                elif i[0] == "DELAY":
                    print("DELAY")
                    Del(i[1], i[2], myTable.table, i[3])
                elif i[0] == "PRINT":
                    print("PRINT")
                    Print(i[1], i[2], myTable)
                elif i[0] == "IF" or i[0] == "ELSEIF":
                    if If(i[1], i[2], i[3], myTable.table, i[4]).Comparison():
                        if i[5] != None:
                            self.runCode(i[5])
                    elif i[6] != None:
                        self.runCode(simpleListBuilder().createListOfLists(i[6]))
                elif i[0] == "FOR":
                    print("FOR")
                    For(i[1], i[2], i[3], i[4], i[5], i[6])

                elif i[0] == "LOOP":
                    print("LOOP")
                    Loop(i[1],i[2]).execute()

                elif i[0] == "WTRUE":
                    print("WHILE TRUE")
                    Wtrue(i[1],i[2]).execute()
                    
                elif i[0] == "BREAK":
                    return True

                elif i[0] == "WHILE":
                    print("WHILE")
                    While(i[1],i[2],i[3],i[4],i[5], myTable.table).execute()


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
            if isinstance(self.value, int) or isinstance(validate_real_bool(self.value), int):
                if type(self.table[self.id]["value"]) == type(self.value):
                    self.table[self.id]["value"] = self.value

                elif type(validate_real_bool(self.table[self.id]["value"])) == type(validate_real_bool(self.value)):
                    self.table[self.id]["value"] = validate_bool(self.value)

                else:
                    errorHandler=Generate_Error(4, self.line)
                    errorHandler.Execute()


            else:
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
        self.table = myTable.table
        self.stringsList = myTable.getStringList()
        self.printLogger = ""
        self.logger = PrintLog()
        self.printChecking()

        print("SE IMPRIMIRA EN LA CONSOLA -->  " + str(self.printLogger) + " DESDE LA LINEA " + str(self.line))

    def printChecking(self):

        for var in self.value:
            if isinstance(var, int):
                self.printLogger = self.printLogger + str(var)
                self.logger.log_print(self.printLogger)
            elif isinstance(validate_real_bool(var), bool):
                self.printLogger = self.printLogger + str(var)
                self.logger.log_print(self.printLogger)
            elif var in self.stringsList:
                self.printLogger = self.printLogger + var[1:-1]
                self.logger.log_print(self.printLogger)
            else:
                exist = False
                for i in self.table:
                    if i == var:
                        exist = True
                        break
                if exist:
                    self.printLogger = self.printLogger + str(self.table[i]["value"]) + " "
                    self.logger.log_print(self.printLogger)
                else:
                    errorHandler = Generate_Error(5, self.line)
                    errorHandler.Execute()

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
            return self.Operate(self.expression1, self.expression2)
        else:
            errorHandler = Generate_Error(5, self.line)
            errorHandler.Execute()
            return False

    def Operate(self, var1, var2):
        accepted = False
        if isinstance(validate_real_bool(var1), bool) and isinstance(validate_real_bool(var2), bool):
            if (self.comparisonSymbol == "=="):
                if (var1 == var2):
                    accepted = True
        elif isinstance(var1, int) and isinstance(var2, int):
            if (self.comparisonSymbol == "=="):
                if (var1 == var2):
                    accepted = True
            elif (self.comparisonSymbol == ">="):
                if (var1 >= var2):
                    accepted = True
            elif (self.comparisonSymbol == "<="):
                if (var1 <= var2):
                    accepted = True
            elif (self.comparisonSymbol == ">"):
                if (var1 > var2):
                    accepted = True
            else:
                if (var1 < var2):
                    accepted = True
        else:
            errorHandler = Generate_Error(14, self.line)
            errorHandler.Execute()
        return accepted

class Opera:
    def __init__(self, operator, operand, operand2,Symbol_table, line):
        self.operator = operator
        self.operand = operand
        self.operand2 = operand2
        self.table = Symbol_table
        self.line = line

    def Operate(self):
        result = None
        var1 = None
        var2 = None

        '''
        Revision del operando 1
        '''

        if not isinstance(self.operand, int): # Operando1 es variable
            for var in self.table:
                if var == str(self.operand):
                    var1 = self.table[var]["value"]
                    print("SOY VAR1 --> " + str(var1))
            if var1 == None:
                print("ES EL 1")
                errorHandler = Generate_Error(5, self.line)
                errorHandler.Execute()
                return
        else:
            var1 = self.operand

        '''
        Revision del operando 2
        '''
        if not isinstance(self.operand2, int): # Operando2 es variable
            for var in self.table:
                if var == str(self.operand2):
                    var2 = self.table[var]["value"]
                    print("SOY VAR2 --> " + str(var2))

            if var2 == None:
                errorHandler = Generate_Error(5, self.line)
                errorHandler.Execute()
                return
        else:
            var2 = self.operand2

        '''
        Resuelve la operacion.. 
        '''
        if isinstance(var1, int) and isinstance(var2, int):
            if self.operator == "+":
                result= var1 + var2
            elif self.operator == "-":
                result=  var1 - var2
            elif self.operator == "/":
                result=  var1 / var2
            elif self.operator == "**":
                result=  var1 ** var2
            elif self.operator == "*":
                result= var1 * var2
        else:
            errorHandler = Generate_Error(6, self.line)
            errorHandler.Execute()
            return
        print("SE DETECTO UN OPERA DE FORMA (" + str(self.operator) + "," + str(var1) + "," + str(var2) + ")" + " CON RESULTADO " + str(result) + " EN LA LINEA " + str(self.line))
        return result


class Loop:
    def __init__(self, instructions,line):
        self.line = line
        self.instructions = instructions
        print("SOY LAS INSTRUCCIONES ---> " + str(self.instructions))

    def execute(self):
        exist = False;
        for ins in self.instructions:
            print("SOY LAS INS ---> " + str(ins))
            if ins[0] == "BREAK":
                exist = True
            elif ins[0] == "IF" or ins[0] == "ELSEIF":
                for i in ins[5]:
                    print("SOY LAS I ---> " + str(i))
                    if i[0] == "BREAK":
                        exist = True
            elif ins[0] == "FOR":
                for i in ins[5]:
                    if i[0] == "BREAK":
                        exist = True

        if exist:
            if Main(None).runCode(self.instructions):
                print("LOOP EJECUTADO")
            else:
                print("SIGUIENTE INSTRUCCION")
        else:
            errorHandler = Generate_Error(17, self.line)
            errorHandler.Execute()


class Wtrue:
    def __init__(self, instructions, line):
        self.line = line
        self.instructions = instructions
        print("WHILE_TRUE")

    def execute(self):
        exist = False;
        for ins in self.instructions:
            if ins[0] == "BREAK":
                exist = True
            elif ins[0] == "IF" or ins[0] == "ELSEIF":
                for i in ins[5]:
                    if i[0] == "BREAK":
                        exist = True
            elif ins[0] == "FOR":
                for i in ins[5]:
                    if i[0] == "BREAK":
                        exist = True
        if exist:
            if Main(None).runCode(self.instructions):
                print("WHILE TRUE EJECUTADO")
            else:
                print("SIGUIENTE INSTRUCCION")
        else:
            errorHandler = Generate_Error(17, self.line)
            errorHandler.Execute()

class While:
    def __init__(self, expr1,compare,expr2,instructions,line,table):
        self.line = line
        self.expr1 = expr1
        self.expr2 = expr2
        self.compare = compare
        self.instructions = instructions
        self.table = table
        self.t_expr1 = None
        self.t_expr2 = None


        print("WHILE")
    def getExpr(self, expr):
        if isinstance(int(expr), int):
            return int(expr)
        if isinstance(validate_real_bool(expr), bool):
            return  validate_real_bool(expr)
        exists = False
        for var in self.table:
            if var == str(expr):
                if self.table[expr]["value"] != None:
                    return self.table[expr]["value"]
                else:
                    errorHandler = Generate_Error(18, self.line)
                    errorHandler.Execute()
        if not exists:
            errorHandler = Generate_Error(5, self.line)
            errorHandler.Execute()

    def execute(self):

        '''
        Comparaciones
        '''
        valid = False
        total_recursion = 0

        self.t_expr1 = self.getExpr(self.expr1)
        self.t_expr2 = self.getExpr(self.expr2)

        if type(self.t_expr1) == type(self.t_expr2):
            if self.compare == "==":
                if self.t_expr1 == self.t_expr2:
                    valid = True
                else:
                    valid = False

            if self.compare == "!=":
                if self.t_expr1 != self.t_expr2:
                    valid = True
                else:
                    valid = False

            if self.compare == ">":
                if self.t_expr1 > self.t_expr2:
                    valid = True
                else:
                    valid = False

            if self.compare == ">=":
                if self.t_expr1 >= self.t_expr2:
                    valid = True
                else:
                    valid = False

            if self.compare == "<":
                if self.t_expr1 < self.t_expr2:
                    valid = True
                else:
                    valid = False

            if self.compare == "<=":
                if self.t_expr1 <= self.t_expr2:
                    valid = True
                else:
                    valid = False

        else:
            errorHandler = Generate_Error(8, self.line)
            errorHandler.Execute()

        if total_recursion < 900:
            if valid:
                Main(None).runCode(self.instructions)
                total_recursion +=1

            else:
                print("WHILE EJECUTADO")

        else:
            errorHandler = Generate_Error(19, self.line)
            errorHandler.Execute()
            #ERROR RECURSION EXCEDIDA

class For:
    def __init__(self, id, const1, range, const2, instructions, line):
        self.id = id
        self.const1 = const1
        self.range = range
        self.const2 = const2
        self.instructions = instructions
        self.line = line
        self.table = myTable.table

        for var in self.table:
            if var == self.id:
                if self.table[var]["value"] != None:
                    errorHandler = Generate_Error(15, self.line)
                    errorHandler.Execute()
                else:
                    if self.const1 <= self.const2:
                        self.table[var]["type"] = int
                        self.runFor()
                    else:
                        errorHandler = Generate_Error(16, self.line)
                        errorHandler.Execute()

    def runFor(self):
        loops = self.const2 - self.const1

        for i in range(loops):
            self.table[self.id]["value"] = self.const1 + i
            Main(None).runCode(self.instructions)

        self.table[self.id]["value"] = None
        self.table[self.id]["type"] = None


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

    def createListOfLists(self, lists):
        simpleList = []
        if isinstance(lists[0], list):
            for i in lists:
                if not isinstance(i[0], list):
                    sublists = []
                    for j in i:
                            sublists.append(j)
                    simpleList.append(sublists)
                else:
                    simpleList += self.createListOfLists(i)
        else:
            simpleList = [lists]
        return simpleList
