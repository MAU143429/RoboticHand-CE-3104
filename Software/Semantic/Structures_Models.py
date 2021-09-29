from Hardware.Robotic_Hand.Translator import Translator
from Software.Semantic.reserved import *
from Software.Semantic.Generate_Error import *
from Software.Semantic.BooleanValue import *
from Software.SymbolsTable import *
myTable = SymbolsTable()
from Software.Print_Log import *

stop = False
class Main():
    def __init__(self, instructions):
        self.instructions = instructions
        if self.instructions != None:
            for i in self.instructions:
                if i[0] == "MAIN":
                    if i[1] != None:
                        self.runCode(i[1])

    def validateOpera(self, operator, operand1, operand2, line):
        if isinstance(operand1, list):
            operand1 = self.validateOpera(operand1[1], operand1[2], operand1[3], operand1[4])
        if isinstance(operand2, list):
            operand2 = self.validateOpera(operand2[1], operand2[2], operand2[3], operand2[4])
        return Opera(operator, operand1, operand2, myTable.table, line).Operate()

    def runCode(self, functionInstructions):
        global stop
        print(functionInstructions)
        if functionInstructions != None:
            for i in functionInstructions:
                if i[0] == "LET":
                    print("LET")
                    if isinstance(i[2], list):
                        if i[2][0] == "OPERA":
                            print("OPERA")
                            operation = self.validateOpera(i[2][1], i[2][2], i[2][3], i[2][4])
                            result = myTable.insertValue(operation, i[1], i[3])
                            Let(i[1], operation, i[3], myTable.table, result)
                    else:
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
                    print("DETECTE QUE TENGO QUE PARAR")
                    stop = True


                elif i[0] == "WHILE":
                    print("WHILE")
                    While(i[1],i[2],i[3],i[4],i[5], myTable.table).execute()

                elif i[0] == "DECLARATION":
                    print("DECLARATION")
                    for j in self.instructions:
                        if j[1] == i[1]:
                            Procedure(i[2], j[2], j[3], myTable.table, i[3], j[4])

class Procedure:
    def __init__(self, declarationParams, procedureParams, instructions, table, line, lineP):
        self.declarationParams = declarationParams
        self.procedureParams = procedureParams
        self.instructions = instructions
        self.table = table
        self.line = line
        self.lineP = lineP

        if len(declarationParams) == len(procedureParams):
            if declarationParams[0] != None:
                exist = False
                for i in procedureParams:
                    for param in self.table:
                        if (param == i):
                            if self.table[param]["value"] != None:
                                errorHandler = Generate_Error(15, self.lineP)
                                errorHandler.Execute()
                                exist = True
                                break
                    if exist:
                        break
                if not exist:
                    if self.validateParams(declarationParams):
                        var = 0
                        while len(declarationParams) != var:
                            self.table[procedureParams[var]]["value"] = declarationParams[var]
                            if isinstance(self.table[procedureParams[var]]["value"], int):
                                self.table[procedureParams[var]]["type"] = int
                            elif isinstance(validate_real_bool(self.table[procedureParams[var]]["value"]), bool):
                                self.table[procedureParams[var]]["type"] = bool
                            var += 1
                        Main(None).runCode(self.instructions)
                        #for j in procedureParams:
                            #self.table[j]["value"] = None

        else:
            errorHandler = Generate_Error(20, self.line)
            errorHandler.Execute()

    def validateParams(self, params):
        errorFound = False
        param = 0
        for i in params:
            exist = True
            if not isinstance(validate_real_bool(i), bool) or isinstance(i, int):
                for var in self.table:
                    if (var == i):
                        if self.table[var]["value"] != None:
                            exist = True
                            self.declarationParams[param] = self.table[var]["value"]
                            break
                        else:
                            exist = False
            if not exist:
                errorFound = True
                errorHandler = Generate_Error(5, self.line)
                errorHandler.Execute()
            param += 1
        if errorFound == False:
            return True
        else:
            return False

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
                    errorHandler=Generate_Error(15, self.line)
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

        if isinstance(self.getExpr(self.value), int):
            if self.checker.check_units():
                print("SE HA REGISTRADO EL DELAY CON DURACION DE " + str(self.getExpr(self.value)) + " " + self.unit +  " EN LA LINEA " + str(self.line))
                t = Translator()
                t.Create_Delay(self.getExpr(self.value),self.unit)
            else:
                e_msg = "SYNTAX ERROR AT LINE " + str(self.line) + ". INVALID TIME SUFFIX"
                errorHandler = Generate_Error(9, self.line)
                errorHandler.Execute()
        else:
            errorHandler = Generate_Error(4, self.line)
            errorHandler.Execute()

    def getExpr(self, expr):
        exists = False
        for var in self.table:
            if var == str(expr):
                if self.table[expr]["value"] != None:
                    return self.table[expr]["value"]
                else:
                    errorHandler = Generate_Error(18, self.line)
                    errorHandler.Execute()
        if isinstance(int(expr), int):
            return int(expr)
        if isinstance(validate_real_bool(expr), bool):
            return  validate_real_bool(expr)
        if not exists:
            errorHandler = Generate_Error(5, self.line)
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
            if var1 == None:
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
    def __init__(self, instructions, line):
        self.line = line
        self.instructions = instructions
        self.stop = False

        print("SOY LAS INSTRUCCIONES ---> " + str(self.instructions))

    def execute(self):
        global stop
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
            total_recursion = 0
            while not stop:
                if total_recursion < 200:
                    print("SOY EL TOTAL RECURSION --> " + str(total_recursion))
                    Main(None).runCode(self.instructions)
                    print("Ejecutando")
                    total_recursion += 1
                else:
                    errorHandler = Generate_Error(19, self.line)
                    errorHandler.Execute()
                    break
            stop = False

        else:
            errorHandler = Generate_Error(17, self.line)
            errorHandler.Execute()


class Wtrue:
    def __init__(self, instructions, line):
        self.line = line
        self.instructions = instructions
        print("WHILE_TRUE")

    def execute(self):
        global stop
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
            total_recursion = 0
            while not stop:
                if total_recursion < 200:
                    Main(None).runCode(self.instructions)
                    print("Ejecutando")
                    total_recursion += 1
                else:
                    errorHandler = Generate_Error(19, self.line)
                    errorHandler.Execute()
                    break
            stop = False

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
        exists = False
        for var in self.table:
            if var == str(expr):
                if self.table[expr]["value"] != None:
                    return self.table[expr]["value"]
                else:
                    errorHandler = Generate_Error(18, self.line)
                    errorHandler.Execute()
        if isinstance(int(expr), int):
            return int(expr)
        if isinstance(validate_real_bool(expr), bool):
            return  validate_real_bool(expr)
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
                while self.t_expr1 == self.t_expr2:
                    if total_recursion < 200:
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        Main(None).runCode(self.instructions)
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        total_recursion += 1
                    else:
                        errorHandler = Generate_Error(19, self.line)
                        errorHandler.Execute()
                        break

            if self.compare == "!=":
                while self.t_expr1 != self.t_expr2:
                    if total_recursion < 200:
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        Main(None).runCode(self.instructions)
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        total_recursion +=1
                    else:
                        errorHandler = Generate_Error(19, self.line)
                        errorHandler.Execute()
                        break
            if self.compare == ">":
                while self.t_expr1 > self.t_expr2:
                    if total_recursion < 200:
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        Main(None).runCode(self.instructions)
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                    else:
                        errorHandler = Generate_Error(19, self.line)
                        errorHandler.Execute()
                        break

            if self.compare == ">=":
                while self.t_expr1 >= self.t_expr2:
                    if total_recursion < 200:
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        Main(None).runCode(self.instructions)
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                    else:
                        errorHandler = Generate_Error(19, self.line)
                        errorHandler.Execute()
                        break

            if self.compare == "<":
                while self.t_expr1 < self.t_expr2:
                    if total_recursion < 200:
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        Main(None).runCode(self.instructions)
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                    else:
                        errorHandler = Generate_Error(19, self.line)
                        errorHandler.Execute()
                        break

            if self.compare == "<=":
                while self.t_expr1 <= self.t_expr2:
                    if total_recursion < 200:
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        Main(None).runCode(self.instructions)
                        self.t_expr1 = self.getExpr(self.expr1)
                        self.t_expr2 = self.getExpr(self.expr2)
                        total_recursion += 1
                    else:
                        errorHandler = Generate_Error(19, self.line)
                        errorHandler.Execute()
                        break
        else:
            errorHandler = Generate_Error(8, self.line)
            errorHandler.Execute()

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
        if self.range == "..=":
            loops = self.const2+1 - self.const1
        else:
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
