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
            clone = lexer.clone()
            clone.input(source)

            for token in clone:
                myTable.insertToken(token.type, token.value)
            myTable.printTable()

            parser = yacc.yacc()
            parser.parse(source)
            myTable.printTable()
            print("Saliendo del parser...")
            print("TERMINE DE COMPILAR")

    else:
        print("ESTA VACIO")
    for Tok in lexer:
        print(Tok)

lex_test()
