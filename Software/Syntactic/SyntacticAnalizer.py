import ply.yacc as yacc
import time
from Tokenize import tokens
from Software.Semantic.Structures_Models import Let
from Software.Semantic.Structures_Models import Del
from sys import stdin


precedence = (
    ('left', 'LET'),
    ('left', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)


def p_calc(p):
      ''' line : variable '''
      print(p[0])

def p_variable(p):

    '''
    variable : LET ID ASSIGN expression SEMICOLON

    '''
    line = p.lineno(2)
    p[0] = Let(p[2], p[4], line)


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

def p_delay(p):

    '''
    line : DELAY LPAREN QUOT INT QUOT RPAREN SEMICOLON

    '''
    line = p.lineno(2)
    p[0] = Del(p[4], line)

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print("Syntax error found!",p)
    print("Error en la linea " + str(p.lineno) + " " + str(p))




