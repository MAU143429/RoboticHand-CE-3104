import ply.yacc as yacc
from Tokenize import tokens
from Software.Semantic.Structures_Models import *
from sys import stdin

precedence = (
    ('right', 'LET'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)

def p_program(p):
    '''
    line : variable
         | delay
         | println
         | opera
         | empty
    '''

'''
###########################################################################
REGLAS PARA LET
###########################################################################
'''
def p_variable(p):
    '''
    variable : LET ID ASSIGN expression SEMICOLON line
    '''
    line = p.lineno(2)
    p[0] = Let(p[2], p[4],line)

def p_expression(p):
    '''
    expression : INT
               | TRUE
               | FALSE
    '''
    p[0] = p[1]
    
def p_expression_var(p):
    '''
    expression : ID
    '''
    p[0] = ('let', p[1])

'''
###########################################################################
REGLAS PARA DELAY
###########################################################################
'''

def p_delay(p):
    '''
    delay : DELAY LPAREN INT COMMA unit RPAREN SEMICOLON line
    '''
    line = p.lineno(2)
    p[0] = Del(p[3],p[5],line)

def p_unit(p):
    '''
    unit : QUOT MIN QUOT
         | QUOT MIL QUOT
         | QUOT SEG QUOT
    '''
    p[0] = p[2]
'''
###########################################################################
REGLAS PARA PRINTLN!
###########################################################################
'''
def p_println(p):
    '''
    println : PRINT EXPR LPAREN QUOT text QUOT RPAREN SEMICOLON line

    '''
    line = p.lineno(2)
    p[0] = Print(p[5], line)


def p_text(p):
    '''
    text : ID

    '''
    p[0] = p[1]
'''
###########################################################################
REGLAS PARA OPERA
###########################################################################
'''
def p_opera(p):
    '''
    opera : OPERA LPAREN operators COMMA operand COMMA operand RPAREN SEMICOLON line
    '''
    line = p.lineno(2)
    p[0] = Opera(p[3], p[5], p[7], line)

def p_operators(p):
    '''
    operators : PLUS
              | MINUS
              | DIVIDE
              | ASTR
              | TIMES
    '''
    p[0] = p[1]

def p_operand(p):
    '''
    operand : INT
            | ID
            | OPERA
    '''
    p[0] = p[1]

def p_error(p):

    print("Syntax error found!", p)
    print("Error on line " + str(p.lineno))
    
def p_empty(p):
    '''
    empty :
    '''
    pass
    #p[0] = None











