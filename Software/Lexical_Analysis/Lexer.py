import ply.lex as lex
import sys
#Dictionary for keywords
reserved = {
        'if': 'IF',
        'else if': 'ELSEIF',
        'else': 'ELSE',
        'while': 'WHILE',
        'let': 'LET',
        'for': 'FOR',
        'loop': 'LOOP',
        'fn': 'FN',
        'integer': 'INTEGER',
        'True': 'TRUE',
        'False': 'FALSE',
        'range': 'RANGE',
        'break': 'BREAK',
        'main': 'MAIN',
        'return': 'RETURN',

    }
class Lexer(object):
    global reserved
    
    # Regular expression rules for simple tokens
    t_EQEQ    = r'\=='
    t_ARROW   = r'\->'
    t_POINTS  = r'\..'
    # List of token names. 
    tokens = (
       'INT',
       'EQEQ',
       'ARROW',
       'POINTS',
       'ID',

    ) + tuple(reserved.values())

    literals = ['{', '}', ';', '(', ')', '+', '-', '*', '/', '=', '<', '>']
    def t_FN(self, t):
        r'\fn'
        t.type = 'FN'
        t.value = 'fn'
        return t
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_][a-zA-Z_][a-zA-Z_0-9+#+_+?]*'
        t.type = reserved.get(t.value,'ID')    # Check for reserved words
        return t
 # Define a rule so we can track line numbers
    def t_INT(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters
    t_ignore  = ' \t'
    t_ignore_COMMENT  = r'\@.*'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0] ,"at line %s"% t.lexer.lineno)
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)

# Build the lexer and try it out
m = Lexer()
m.build()  
# Test it out
data = '''

let esbueno?_# = 49;
@declarar var
let bc = True
3 + 4 * 10;
while True{
    let parte = 90
}
loop{
    break;
}
else if True{
    let acy# = 0;
}
fn main(){
    return;

}
'''         # Build the lexer
m.test(data)     # Test it