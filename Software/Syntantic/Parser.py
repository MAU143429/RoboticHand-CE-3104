import ply.yacc as yacc
from Keywords import *



def build(lex):


    def p_value(p):
        '''
        value : expresion
              | empty
        '''

    syntactic = yacc.yacc()
