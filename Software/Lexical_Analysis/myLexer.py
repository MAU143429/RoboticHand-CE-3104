import ply.lex as lex
import ply.yacc as yacc
from LexicalAnalizer import *
from Software.Syntactic.SyntacticAnalizer import *

sourceFile = "test.txt"
def lex_test(sourceFile):
    lexer = lex.lex()
    parser = yacc.yacc()
    if sourceFile is not None:
                with open(sourceFile) as file:
                    source = file.read()
                    lexer.input(source)
                    '''
                    data = " "
                    for line in file:
                        data += '\n' + line
                    print(data)
                    '''
                    print(source)
                    parser.parse(source);
    for Tok in lexer:
        print(Tok)

lex_test(sourceFile)


