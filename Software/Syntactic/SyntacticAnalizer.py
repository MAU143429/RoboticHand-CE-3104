import ply.yacc as yacc
from Software.Lexical_Analysis.Tokenize import tokens
from Software.Lexical_Analysis.LexicalAnalizer import *
from Software.Semantic.Structures_Models import *
from sys import stdin

precedence = (
    ('right', 'LET'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)

def p_main(p):
    '''
    main : FN MAIN LPAREN RPAREN LCRLBRACKET line RCRLBRACKET
    '''

def p_program(p):
    '''
    line : loop
         | for
         | let
         | move
         | delay
         | println
         | empty
    '''

'''
###########################################################################
REGLAS PARA LOOP
###########################################################################
'''
def p_loop(p):
    '''
    loop : LOOP LCRLBRACKET line RCRLBRACKET line
    '''
    line = p.lineno(2)
    p[0] = Loop(line)

'''
###########################################################################
REGLAS PARA FOR
###########################################################################
'''

def p_for(p):
    '''
    for : FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET line
    '''
    line = p.lineno(2)
    p[0] = For(p[2], p[4], p[5], p[6], line)

'''
###########################################################################
REGLAS PARA MOVE
###########################################################################
'''
def p_move(p):
    '''
    move : MOVE LPAREN QUOT ID QUOT COMMA expression RPAREN SEMICOLON line
    '''
    line = p.lineno(2)
    p[0] = Move(p[4], p[7], line)

def p_finger(p):
    '''
    finger : P
           | I
           | M
           | A
           | Q
           | T
    '''
    p[0] = p[1]

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
REGLAS PARA LET
###########################################################################
'''
def p_let(p):
    '''
    let : LET ID ASSIGN INT SEMICOLON line
             | LET ID ASSIGN expression SEMICOLON line
    '''
    line = p.lineno(2)
    p[0] = Let(p[2], p[4], line)


def p_expression_bool(p):
    '''
    expression : TRUE
               | FALSE
               | ID
               | opera
    '''
    p[0] = p[1]

'''
###########################################################################
REGLAS PARA OPERA
###########################################################################
'''
def p_opera(p):
    '''
    opera : OPERA LPAREN operator COMMA operand COMMA operand RPAREN
    '''
    line = p.lineno(2)
    p[0] = Opera(p[3], p[5], p[7], line).Operate()

def p_operators(p):
    '''
    operator : PLUS
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
            | opera
    '''
    p[0] = p[1]

def p_error(p):

    print("Syntax error found!", p)
    if not p == None:
        print("Error on line " + str(p.lineno))
    
def p_empty(p):
    '''
    empty :
    '''
    pass
    #p[0] = None











