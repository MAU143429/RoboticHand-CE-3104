import ply.lex as lex
import ply.yacc as yacc
from Software.Syntactic.SyntacticAnalizer import *


def lex_test():

    sourceFile = "../Lexical_Analysis/source.txt"
    if sourceFile is not None:
        with open(sourceFile, 'r') as file:
            print("Entrando al lexer...")
            try:
                source = file.read()
            except EOFError as e:
                print(e)

            lexer = lex.lex()
            lexer.input(source)
            clone = lexer.clone()
            clone.input(source)
            error = ErrorLog()

            for token in clone:
                myTable.insertToken(token.type, token.value)

            print("esta es mi tabla")
            myTable.printTable()

            if not main_checker():
                print("Voy a crear el parser")
                parser = yacc.yacc()
                parser.parse(source)



            myTable.printTable()
            print("Saliendo del parser...")
            print("TERMINE DE COMPILAR")
            print(" \n *********** ERRORES DE COMPILACION *********** \n")
            error.print()

            print(" \n ******************* FIN ********************** \n")

def main_checker():
    if myTable.mainCounter != 1:
        print("Debe haber un solo main")
        return True
    else:
        return False
lex_test()
