import ply.lex as lex
from Keywords import *
import sys
#Dictionary for keywords


class LexicalAnalizer():

    def __init__(self, sourceFile = None, debugLexer  = False):
        super().__init__()
        self.keywordsCollection = Keywords()
        self.readedTokens = []
        self.sourceFile = sourceFile
        self.debug = debugLexer
        self.Lexer = None

        # List of token names. 
        self.tokens = self.keywordsCollection.tokens
        
        self.literals = self.keywordsCollection.literals

    def BuildLexer(self):
        # Regular expression rules for simple tokens
        tokens = self.tokens
        literals = self.literals
        t_EQEQ    = r'\=='
        t_ARROW   = r'\->'
        t_POINTS  = r'\..'

        def t_FN(t):
            r'fn'
            t.type = 'FN'
            t.value = 'fn'
            return t
        def t_ELSEIF(t):
            r'elseif'
            t.type = 'ELSEIF'
            t.value = 'elseif'
            return t
        def t_ELSE(t):
            r'else'
            t.type = 'ELSE'
            t.value = 'else'
            return t
        def t_IF(t):
            r'if'
            t.type = 'IF'
            t.value = 'if'
            return t
        
        def t_ID(t):
            r'[a-zA-Z_][a-zA-Z_][a-zA-Z_][a-zA-Z_0-9+#+_+?]*'
            t.type = self.keywordsCollection.reserved.get(t.value,'ID') 
            if t.type == 'ID':
                Column = 0

                if len(str(t.value)) > 15:
                    print("Warning: Identifier exceeds maximum length")

                contents = {}
                if self.sourceFile is not None:
                    with open(self.sourceFile) as file:
                        source = file.read()
                        Column = self.FindColumn(source, t)
                contents["TokenLocation"] = (t.lineno, t.lexpos, Column)

                t.value = {"lexeme": t.value, "additional": contents}

            if self.debug == True:
                print(t)

            return t
   
        def t_INT(t):
            r'\d+'
            t.value = int(t.value)
            return t

        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        # A string containing ignored characters
        t_ignore  = ' \t'
        t_ignore_COMMENT  = r'\@.*'

        # Error handling rule
        def t_error(t):
            source = ""
            Column = 0

            if self.sourceFile is not None:
                with open(self.sourceFile) as file:
                    source = file.read()
                    Column = self.FindColumn(source, t)
            else:
                source = t.lexer.lexdata
                Column = self.FindColumn(source, t)

            self.ErrorPrint(self.sourceFile, t.lineno, Column)

            t.lexer.skip(1)
        # Build the lexer
        if self.sourceFile is not None:
                with open(self.sourceFile) as file:
                    source = file.read()
                    self.Lexer = lex.lex()
                    self.Lexer.input(source)
        
   
    def FindColumn(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    def ErrorPrint(self, Source, Lineno, Column):
        arrow = ""

        if self.sourceFile is not None:
            print("\nInvalid token on line {}\n".format(Lineno))
            #print line
            with open(self.sourceFile) as file:
                for i in range(0,Lineno):
                    source = file.readline()
            

            #build arrow
            for i in range(0,Column-1):
                arrow += "-"
            arrow += "^\n"
        print(source)
        print(arrow)

lexer = LexicalAnalizer("Software\Lexical_Analysis\source.txt", False)
lexer.BuildLexer()

for Tok in lexer.Lexer:
        print(Tok)