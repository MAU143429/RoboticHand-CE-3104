import sys
from Software.Syntactic import SyntacticAnalizer as parser
from Software.Error_Log import ErrorLog

class Generate_Error:

    def __init__(self, code , line=0):
        self.code = code
        self.line = line
        self.error = ErrorLog()

    def Execute(self):
        if self.code == 0:
            e_msg = "SYNTAX ERROR 0 ---> SYNTAX INCORRECT"
            parser.semantic_error = True
            self.error.log_error(e_msg, 2)

        if self.code == 1:
            e_msg = "SEMANTIC ERROR: NO MAIN PROCEDURE FOUND"
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 2:
            e_msg = "SEMANTIC ERROR: ONLY ONE MAIN PROCEDURE ALLOWED"
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 3:
            e_msg = "SEMANTIC ERROR: MAIN PROCEDURE CAN´T HAVE PARAMETERS"
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 4:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". DATA TYPE ASSIGNATION MISMATCH"
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 5:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". AN UNDECLARED VARIABLE WAS CALLED"
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 6:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". CAN'T USE ARITHMETIC OPERATOR WITH BOOLEAN DATA " \
                                                                 "TYPE "
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 7:
            e_msg = "RUN-TIME ERROR AT LINE " + str(self.line) + ". INTEGER DIVISION BY ZERO"
            parser.semantic_error = True
            self.error.log_error(e_msg, 2)

        if self.code == 8:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". DATA TYPE ASSIGNATION MISMATCH"
            parser.semantic_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 9:
            e_msg = "SYNTAX ERROR AT LINE " + str(self.line) + ". INVALID TIME SUFFIX"
            parser.syntax_error = True
            print(parser.syntax_error)
            self.error.log_error(e_msg, 2)

        if self.code == 10:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". INVALID FINGER KEYWORD"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 11:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". INVALID FINGER IN A LIST"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 12:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". INVALID MOVEMENT VALUE"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 13:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". INVALID TIME VALUE"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 14:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". CAN´T COMPARE AN INTEGER WITH A BOOLEAN"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 15:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". A DECLARED VARIABLE WAS CALLED"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 16:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". FOR LOOP OUT OF RANGE"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 17:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". MISSING BREAK EXPRESSION"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 18:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". INVALID VARIABLE"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 19:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". MAXIMUM RECURSION DEPTH EXCEEDED IN COMPARISON"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)

        if self.code == 20:
            e_msg = "SEMANTIC ERROR AT LINE " + str(self.line) + ". PARAMETERS DO NOT MATCH"
            parser.syntax_error = True
            self.error.log_error(e_msg, 3)