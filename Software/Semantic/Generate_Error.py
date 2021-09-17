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


        
        