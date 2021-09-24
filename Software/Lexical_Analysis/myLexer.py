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
                if myTable.mainCounter > 1:
                    error_text = "Lexical error at line " + str(token.lineno) + " There can only be one main function"
                    error.log_error(error_text)
                    return
                myTable.insertToken(token.type, token.value)



            print("esta es mi tabla")
            myTable.printTable()
            parser = yacc.yacc()
            parser.parse(source)
            myTable.printTable()
            print("Saliendo del parser...")
            print("TERMINE DE COMPILAR")
            print(" \n *********** ERRORES DE COMPILACION *********** \n")

            error.print()
            print(" \n ******************* FIN ********************** \n")

    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)

lex_test()
