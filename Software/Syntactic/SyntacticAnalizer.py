import ply.yacc as yacc
from Software.Lexical_Analysis.Tokenize import tokens
from Software.Lexical_Analysis.LexicalAnalizer import *
from Software.Semantic.Structures_Models import *
from sys import stdin
from Software.SymbolsTable import *
from Software.Error_Log import ErrorLog

precedence = (
    ('right', 'LET'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)
syntax_error = False
semantic_error = False
myTable = SymbolsTable()





def p_program(p):
    '''
    line : main line
         | loop line
         | for line
         | while line
         | if line
         | if elseiforelse
         | let line
         | move line
         | moveList line
         | delay line
         | println line
         | break line
         | empty
    '''

def p_main(p):
    '''
    main : FN MAIN LPAREN RPAREN LCRLBRACKET line RCRLBRACKET
    '''

'''
###########################################################################
REGLAS PARA LOOP
###########################################################################
'''


def p_loop(p):
    '''
    loop : LOOP LCRLBRACKET line RCRLBRACKET
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
    for : FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET
    '''
    line = p.lineno(2)
    p[0] = For(p[2], p[4], p[5], p[6], line)


'''
###########################################################################
REGLAS PARA WHILE
###########################################################################
'''


def p_while(p):
    '''
    while : WHILE LPAREN expression compare expression RPAREN LCRLBRACKET line RCRLBRACKET
          | WHILE TRUE LCRLBRACKET line RCRLBRACKET
    '''
    line = p.lineno(2)
    p[0] = While(line)


'''
###########################################################################
REGLAS PARA MOVE
###########################################################################
'''


def p_move(p):
    '''
    move : MOVE LPAREN STRING COMMA bool RPAREN SEMICOLON
    '''
    line = p.lineno(2)
    p[0] = Move(p[3], p[5], myTable.table, line)


def p_moveList(p):
    '''
    moveList : MOVE LPAREN LSQRBRACKET fingerList RSQRBRACKET COMMA bool RPAREN SEMICOLON
    '''
    line = p.lineno(2)
    p[0] = Move(simpleListBuilder().createList(p[4]), p[7], myTable.table, line)


def p_fingerList(p):
    '''
    fingerList : STRING COMMA STRING
               | STRING COMMA fingerList
    '''
    p[0] = [p[1], p[3]]


'''
###########################################################################
REGLAS PARA DELAY
###########################################################################
'''


def p_delay(p):
    '''
    delay : DELAY LPAREN INT COMMA STRING RPAREN SEMICOLON
    '''
    line = p.lineno(2)
    p[0] = Del(p[3], p[5], myTable.table, line)


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
    println : PRINT EXPR LPAREN args RPAREN SEMICOLON

    '''
    line = p.lineno(2)
    p[0] = Print(simpleListBuilder().createList(p[4]), line)


def p_args(p):
    '''
    args : INT body
         | ID body
         | opera body
         | TRUE body
         | FALSE body
         | STRING body

    '''
    if not p[2] is None:
        p[0] = [p[1], p[2]]
    else:
        p[0] = p[1]

def p_body(p):
    '''
    body : COMMA args
         | COMMA body
         | empty empty
    '''
    p[0] = p[2]


def p_text(p):
    '''
    text : QUOT ID QUOT
    '''
    p[0] = p[1]


'''
###########################################################################
REGLAS PARA IF, ELSE IF and ELSE
###########################################################################
'''


def p_elseiforelse(p):
    '''
    elseiforelse : elseif line
                 | elseif elseiforelse
                 | else line
    '''


def p_if(p):
    '''
    if : IF expression compare expression LCRLBRACKET line RCRLBRACKET
    '''
    p[0] = If(p[2], p[3], p[4]).Comparison()
    print("if")

def p_elseif(p):
    '''
    elseif : ELSEIF expression compare expression LCRLBRACKET line RCRLBRACKET
    '''
    print("elseif")

def p_else(p):
    '''
    else : ELSE LCRLBRACKET line RCRLBRACKET
    '''
    print("else")

def p_compare(p):
    '''
    compare : EQEQ
            | LTE
            | GTE
            | LT
            | GT
    '''
    p[0] = p[1]

def p_expressions(p):
    '''
    expression : INT
               | TRUE
               | FALSE
               | opera
               | ID
    '''
    p[0] = p[1]

'''
###########################################################################
REGLAS PARA LET
###########################################################################
'''


def p_let(p):
    '''
    let : LET ID ASSIGN operand SEMICOLON
        | LET ID ASSIGN bool SEMICOLON
    '''

    line = p.lineno(2)
    result = myTable.insertValue(p[4],p[2], line)
    p[0] = Let(p[2], p[4], line, myTable.table, result)
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
            | opera
            | ID
    '''
    p[0] = p[1]


def p_expression_bool(p):
    '''
    bool : TRUE
         | FALSE
         | ID
    '''
    p[0] = p[1]


def p_break(p):
    '''
    break : BREAK
    '''
    p[0] = p[1]

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")
    error = ErrorLog()
    error.log_error(f"Syntax error: Unexpected {token}")


def p_empty(p):
    '''
    empty :
    '''
    pass
    # p[0] = None
