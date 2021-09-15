import ply.lex as lex
import ply.yacc as yacc
from LexicalAnalizer import *
from SyntacticAnalizer import *

sourceFile = "Software/Lexical_Analysis/test.txt"
def lex_test(sourceFile):
    lexer = lex.lex()
    parser = yacc.yacc()
    if sourceFile is not None:
                with open(sourceFile) as file:
                    source = file.read()
                    lexer.input(source)
                    parser.parse(source)
    #for Tok in lexer:
    #    print(Tok)

lex_test(sourceFile)


