import sys
from Software.Syntactic import Parser as parser
from Software.Error_Log import ErrorLog

class Generate_Error:

    def __init__(self, code , line=0):
        self.code = code
        self.line = line
        self.error = ErrorLog()

    def Execute(self):
        if self.code == 0:
            e_msg = "SEMANTIC ERROR 0 ---> SYNTAX INCORRECT"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 1:
            e_msg = "SEMANTIC ERROR: NO MAIN PROCEDURE FOUND"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 2:
            e_msg = "SEMANTIC ERROR: ONLY ONE MAIN PROCEDURE ALLOWED"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 3:
            e_msg = "SEMANTIC ERROR: MAIN PROCEDURE CAN´T HAVE PARAMETERS"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 4:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". DATA TYPE ASSIGNATION MISMATCH"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 5:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". AN UNDECLARED VARIABLE WAS CALLED"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 6:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". CAN'T USE ARITHMETIC OPERATOR WITH BOOLEAN DATA " \
                                                                 "TYPE "
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 7:
            e_msg = "RUN-TIME ERROR AT LINE " + str(self.line) + ". INTEGER DIVISION BY ZERO"
            parser.semantic_error = True
            self.error.log_error(e_msg)

        if self.code == 8:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". DATA TYPE ASSIGNATION MISMATCH"
            parser.semantic_error = True
            self.error.log_error(e_msg)


        
        