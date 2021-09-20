import ply.lex as lex
import ply.yacc as yacc
from Software.Syntactic.SyntacticAnalizer import *


def lex_test():
    sourceFile = "../Lexical_Analysis/test.txt"
    if sourceFile is not None:
                with open(sourceFile, 'r') as file:
                    print("Entrando al lexer...")
                    try:
                        source = file.read()
                    except EOFError as e:
                        print(e)

                    lexer = lex.lex()
                    lexer.input(source)
                    print("Lexer listo")
                    print("Entrando al parser...")
                    parser = yacc.yacc()
                    print("Saliendo del parser...")
                    parser.parse(source)
                    print("TERMINE DE COMPILAR")

    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)

lex_test()





