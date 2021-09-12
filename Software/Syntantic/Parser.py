import ply.yacc as yacc
from Keywords import *



def build(lex):
    syntactic = yacc.yacc()
