
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightLETrightASSIGNleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENnonassocUMINUSARROW ASSIGN ASTR BOOLEAN BREAK COMMA DELAY DIVIDE DOTDOT ELSE ELSEIF EQEQ EXPR FALSE FN FOR GT GTE ID IF IN INT INTEGER LCRLBRACKET LET LOOP LPAREN LSQRBRACKET LT LTE MAIN MIL MIN MINUS MOVE OPERA PLUS PRINT QUOT RANGE RCRLBRACKET RETURN RPAREN RSQRBRACKET SEG SEMICOLON STRING TIMES TRUE WHILE WRONG_ID\n    root : main root\n         | function root\n         | procedure root\n         | let root\n         | empty empty\n    \n    functions : ID\n    \n    main : FN MAIN LPAREN RPAREN LCRLBRACKET line RCRLBRACKET\n    \n    line : loop line\n         | function line\n         | procedure line\n         | for line\n         | while line\n         | if line\n         | let line\n         | move line\n         | moveList line\n         | delay line\n         | println line\n         | break line\n         | empty empty\n    \n    procedure : FN ID LPAREN params RPAREN prodbody\n    \n    prodbody : LCRLBRACKET line RCRLBRACKET\n    \n    function : FN ID LPAREN params RPAREN funbody\n    \n    params : ID arg\n          | empty empty\n    \n    arg : COMMA params\n        | COMMA arg\n        | empty empty\n    \n    funbody : ARROW output LCRLBRACKET line end RCRLBRACKET\n    \n    output : INTEGER\n            | BOOLEAN\n    \n    end : RETURN expression SEMICOLON\n    \n    loop : LOOP LCRLBRACKET line RCRLBRACKET\n    \n    for : FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET\n    \n    while : WHILE LPAREN expression compare expression RPAREN LCRLBRACKET line RCRLBRACKET\n          | WHILE TRUE LCRLBRACKET line RCRLBRACKET\n    \n    move : MOVE LPAREN STRING COMMA bool RPAREN SEMICOLON\n    \n    moveList : MOVE LPAREN LSQRBRACKET fingerList RSQRBRACKET COMMA bool RPAREN SEMICOLON\n    \n    fingerList : STRING COMMA STRING\n               | STRING COMMA fingerList\n    \n    delay : DELAY LPAREN INT COMMA STRING RPAREN SEMICOLON\n    \n    unit : QUOT MIN QUOT\n         | QUOT MIL QUOT\n         | QUOT SEG QUOT\n    \n    println : PRINT EXPR LPAREN args RPAREN SEMICOLON\n\n    \n    args : INT body\n         | ID body\n         | opera body\n         | TRUE body\n         | FALSE body\n         | STRING body\n\n    \n    body : COMMA args\n         | COMMA body\n         | empty empty\n    \n    text : QUOT ID QUOT\n    \n    elseiforelse : elseif\n                 | else\n    \n    if : IF expression compare expression LCRLBRACKET line RCRLBRACKET empty\n       | IF expression compare expression LCRLBRACKET line RCRLBRACKET elseiforelse\n    \n    elseif : ELSEIF expression compare expression LCRLBRACKET line RCRLBRACKET empty\n           | ELSEIF expression compare expression LCRLBRACKET line RCRLBRACKET elseiforelse\n    \n    else : ELSE LCRLBRACKET line RCRLBRACKET\n    \n    compare : EQEQ\n            | LTE\n            | GTE\n            | LT\n            | GT\n    \n    expression : INT\n               | TRUE\n               | FALSE\n               | opera\n               | ID\n               | negative\n    \n    let : LET ID ASSIGN operand SEMICOLON\n        | LET ID ASSIGN bool SEMICOLON\n    \n    opera : OPERA LPAREN operator COMMA operand COMMA operand RPAREN\n    \n    operator : PLUS\n             | MINUS\n             | DIVIDE\n             | ASTR\n             | TIMES\n    \n    operand : INT\n            | opera\n            | ID\n            | negative\n    \n    negative : MINUS INT %prec UMINUS\n    \n    bool : TRUE\n         | FALSE\n         | ID\n    \n    break : BREAK\n    \n    empty :\n    '
    
_lr_action_items = {'FN':([0,2,3,4,5,34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,81,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[7,7,7,7,7,44,-74,-75,44,44,44,44,44,44,44,44,44,44,44,44,-90,-23,-21,44,-7,44,44,44,-22,-33,-36,44,-45,-29,44,44,-91,-37,-41,-58,-59,-56,-57,-34,-35,44,-38,-62,44,-91,-60,-61,]),'LET':([0,2,3,4,5,34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,81,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[8,8,8,8,8,8,-74,-75,8,8,8,8,8,8,8,8,8,8,8,8,-90,-23,-21,8,-7,8,8,8,-22,-33,-36,8,-45,-29,8,8,-91,-37,-41,-58,-59,-56,-57,-34,-35,8,-38,-62,8,-91,-60,-61,]),'$end':([0,1,2,3,4,5,6,9,10,11,12,13,40,41,71,72,81,130,184,],[-91,0,-91,-91,-91,-91,-91,-1,-2,-3,-4,-5,-74,-75,-23,-21,-7,-22,-29,]),'MAIN':([7,],[14,]),'ID':([7,8,18,19,36,44,60,62,97,114,119,120,121,122,123,124,128,135,138,150,162,170,176,200,208,],[15,16,21,24,21,15,96,104,104,132,104,-63,-64,-65,-66,-67,144,104,156,132,144,104,156,104,104,]),'LPAREN':([14,15,32,61,63,64,108,],[17,18,42,97,106,107,128,]),'ASSIGN':([16,],[19,]),'RPAREN':([17,18,21,22,23,27,28,29,30,31,35,36,37,39,43,67,68,69,70,100,101,102,103,104,105,109,132,142,143,144,145,146,147,148,152,155,156,159,161,162,163,164,165,166,167,168,171,181,182,183,186,191,],[20,-91,-91,38,-91,-82,-83,-85,-87,-88,-24,-91,-91,-25,-86,-26,-27,-91,-28,-68,-69,-70,-71,-72,-73,-25,-84,160,-91,-91,-91,-91,-91,-91,173,175,-89,179,-46,-91,-91,-47,-48,-49,-50,-51,186,-52,-53,-54,-76,202,]),'INT':([19,33,62,97,107,114,116,119,120,121,122,123,124,128,135,150,151,162,170,200,208,],[27,43,100,100,127,27,134,100,-63,-64,-65,-66,-67,143,100,27,172,143,100,100,100,]),'TRUE':([19,61,62,97,119,120,121,122,123,124,128,135,138,162,170,176,200,208,],[30,98,101,101,101,-63,-64,-65,-66,-67,146,101,30,146,101,30,101,101,]),'FALSE':([19,62,97,119,120,121,122,123,124,128,135,138,162,170,176,200,208,],[31,102,102,102,-63,-64,-65,-66,-67,147,102,31,147,102,31,102,102,]),'OPERA':([19,62,97,114,119,120,121,122,123,124,128,135,150,162,170,200,208,],[32,32,32,32,32,-63,-64,-65,-66,-67,32,32,32,32,32,32,32,]),'MINUS':([19,42,62,97,114,119,120,121,122,123,124,135,150,170,200,208,],[33,77,33,33,33,33,-63,-64,-65,-66,-67,33,33,33,33,33,]),'LCRLBRACKET':([20,38,43,59,98,100,101,102,103,104,105,110,111,112,137,172,173,186,201,210,],[34,74,-86,95,118,-68,-69,-70,-71,-72,-73,129,-30,-31,154,187,188,-76,206,212,]),'COMMA':([21,27,28,29,36,43,75,76,77,78,79,80,125,127,131,132,140,143,144,145,146,147,148,157,162,177,186,],[36,-82,-83,-85,36,-86,114,-77,-78,-79,-80,-81,138,141,150,-84,158,162,162,162,162,162,162,176,162,158,-76,]),'SEMICOLON':([24,25,26,27,28,29,30,31,43,100,101,102,103,104,105,160,175,179,185,186,202,],[-84,40,41,-82,-83,-85,-87,-88,-86,-68,-69,-70,-71,-72,-73,180,190,192,193,-76,207,]),'LOOP':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[59,-74,-75,59,59,59,59,59,59,59,59,59,59,59,59,-90,-23,-21,59,59,59,59,-22,-33,-36,59,-45,-29,59,59,-91,-37,-41,-58,-59,-56,-57,-34,-35,59,-38,-62,59,-91,-60,-61,]),'FOR':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[60,-74,-75,60,60,60,60,60,60,60,60,60,60,60,60,-90,-23,-21,60,60,60,60,-22,-33,-36,60,-45,-29,60,60,-91,-37,-41,-58,-59,-56,-57,-34,-35,60,-38,-62,60,-91,-60,-61,]),'WHILE':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[61,-74,-75,61,61,61,61,61,61,61,61,61,61,61,61,-90,-23,-21,61,61,61,61,-22,-33,-36,61,-45,-29,61,61,-91,-37,-41,-58,-59,-56,-57,-34,-35,61,-38,-62,61,-91,-60,-61,]),'IF':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[62,-74,-75,62,62,62,62,62,62,62,62,62,62,62,62,-90,-23,-21,62,62,62,62,-22,-33,-36,62,-45,-29,62,62,-91,-37,-41,-58,-59,-56,-57,-34,-35,62,-38,-62,62,-91,-60,-61,]),'MOVE':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[63,-74,-75,63,63,63,63,63,63,63,63,63,63,63,63,-90,-23,-21,63,63,63,63,-22,-33,-36,63,-45,-29,63,63,-91,-37,-41,-58,-59,-56,-57,-34,-35,63,-38,-62,63,-91,-60,-61,]),'DELAY':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[64,-74,-75,64,64,64,64,64,64,64,64,64,64,64,64,-90,-23,-21,64,64,64,64,-22,-33,-36,64,-45,-29,64,64,-91,-37,-41,-58,-59,-56,-57,-34,-35,64,-38,-62,64,-91,-60,-61,]),'PRINT':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[65,-74,-75,65,65,65,65,65,65,65,65,65,65,65,65,-90,-23,-21,65,65,65,65,-22,-33,-36,65,-45,-29,65,65,-91,-37,-41,-58,-59,-56,-57,-34,-35,65,-38,-62,65,-91,-60,-61,]),'BREAK':([34,40,41,46,47,48,49,50,51,52,53,54,55,56,57,66,71,72,74,95,118,129,130,133,153,154,180,184,187,188,189,190,192,196,197,198,199,203,204,206,207,211,212,214,215,216,],[66,-74,-75,66,66,66,66,66,66,66,66,66,66,66,66,-90,-23,-21,66,66,66,66,-22,-33,-36,66,-45,-29,66,66,-91,-37,-41,-58,-59,-56,-57,-34,-35,66,-38,-62,66,-91,-60,-61,]),'RCRLBRACKET':([34,40,41,45,46,47,48,49,50,51,52,53,54,55,56,57,58,66,71,72,74,82,83,84,85,86,87,88,89,90,91,92,93,94,95,113,115,118,130,133,136,153,154,169,174,180,184,187,188,189,190,192,193,194,195,196,197,198,199,203,204,206,207,209,211,212,213,214,215,216,],[-91,-74,-75,81,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-90,-23,-21,-91,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-91,130,133,-91,-22,-33,153,-36,-91,184,189,-45,-29,-91,-91,-91,-37,-41,-32,203,204,-58,-59,-56,-57,-34,-35,-91,-38,211,-62,-91,214,-91,-60,-61,]),'ARROW':([38,],[73,]),'RETURN':([40,41,46,47,48,49,50,51,52,53,54,55,56,57,58,66,71,72,82,83,84,85,86,87,88,89,90,91,92,93,94,129,130,133,149,153,180,184,189,190,192,196,197,198,199,203,204,207,211,214,215,216,],[-74,-75,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-90,-23,-21,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-91,-22,-33,170,-36,-45,-29,-91,-37,-41,-58,-59,-56,-57,-34,-35,-38,-62,-91,-60,-61,]),'PLUS':([42,],[76,]),'DIVIDE':([42,],[78,]),'ASTR':([42,],[79,]),'TIMES':([42,],[80,]),'EQEQ':([43,99,100,101,102,103,104,105,117,186,205,],[-86,120,-68,-69,-70,-71,-72,-73,120,-76,120,]),'LTE':([43,99,100,101,102,103,104,105,117,186,205,],[-86,121,-68,-69,-70,-71,-72,-73,121,-76,121,]),'GTE':([43,99,100,101,102,103,104,105,117,186,205,],[-86,122,-68,-69,-70,-71,-72,-73,122,-76,122,]),'LT':([43,99,100,101,102,103,104,105,117,186,205,],[-86,123,-68,-69,-70,-71,-72,-73,123,-76,123,]),'GT':([43,99,100,101,102,103,104,105,117,186,205,],[-86,124,-68,-69,-70,-71,-72,-73,124,-76,124,]),'EXPR':([65,],[108,]),'INTEGER':([73,],[111,]),'BOOLEAN':([73,],[112,]),'IN':([96,],[116,]),'STRING':([106,126,128,141,158,162,],[125,140,148,159,177,148,]),'LSQRBRACKET':([106,],[126,]),'DOTDOT':([134,],[151,]),'RSQRBRACKET':([139,177,178,],[157,-39,-40,]),'ELSEIF':([189,214,],[200,200,]),'ELSE':([189,214,],[201,201,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,2,3,4,5,],[1,9,10,11,12,]),'main':([0,2,3,4,5,],[2,2,2,2,2,]),'function':([0,2,3,4,5,34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[3,3,3,3,3,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'procedure':([0,2,3,4,5,34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[4,4,4,4,4,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'let':([0,2,3,4,5,34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[5,5,5,5,5,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'empty':([0,2,3,4,5,6,18,21,23,34,36,37,46,47,48,49,50,51,52,53,54,55,56,57,58,69,74,95,118,129,143,144,145,146,147,148,154,162,163,187,188,189,206,212,214,],[6,6,6,6,6,13,23,37,39,58,69,70,58,58,58,58,58,58,58,58,58,58,58,58,94,109,58,58,58,58,163,163,163,163,163,163,58,163,183,58,58,196,58,58,215,]),'params':([18,36,],[22,67,]),'operand':([19,114,150,],[25,131,171,]),'bool':([19,138,176,],[26,155,191,]),'opera':([19,62,97,114,119,128,135,150,162,170,200,208,],[28,103,103,28,103,145,103,28,145,103,103,103,]),'negative':([19,62,97,114,119,135,150,170,200,208,],[29,105,105,29,105,105,29,105,105,105,]),'arg':([21,36,],[35,68,]),'line':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[45,82,83,84,85,86,87,88,89,90,91,92,93,113,115,136,149,174,194,195,209,213,]),'loop':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'for':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'while':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'if':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'move':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'moveList':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'delay':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'println':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'break':([34,46,47,48,49,50,51,52,53,54,55,56,57,74,95,118,129,154,187,188,206,212,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'funbody':([38,],[71,]),'prodbody':([38,],[72,]),'operator':([42,],[75,]),'expression':([62,97,119,135,170,200,208,],[99,117,137,152,185,205,210,]),'output':([73,],[110,]),'compare':([99,117,205,],[119,135,208,]),'fingerList':([126,158,],[139,178,]),'args':([128,162,],[142,181,]),'body':([143,144,145,146,147,148,162,],[161,164,165,166,167,168,182,]),'end':([149,],[169,]),'elseiforelse':([189,214,],[197,216,]),'elseif':([189,214,],[198,198,]),'else':([189,214,],[199,199,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> main root','root',2,'p_root','SyntacticAnalizer.py',23),
  ('root -> function root','root',2,'p_root','SyntacticAnalizer.py',24),
  ('root -> procedure root','root',2,'p_root','SyntacticAnalizer.py',25),
  ('root -> let root','root',2,'p_root','SyntacticAnalizer.py',26),
  ('root -> empty empty','root',2,'p_root','SyntacticAnalizer.py',27),
  ('functions -> ID','functions',1,'p_functions','SyntacticAnalizer.py',38),
  ('main -> FN MAIN LPAREN RPAREN LCRLBRACKET line RCRLBRACKET','main',7,'p_main','SyntacticAnalizer.py',43),
  ('line -> loop line','line',2,'p_program','SyntacticAnalizer.py',49),
  ('line -> function line','line',2,'p_program','SyntacticAnalizer.py',50),
  ('line -> procedure line','line',2,'p_program','SyntacticAnalizer.py',51),
  ('line -> for line','line',2,'p_program','SyntacticAnalizer.py',52),
  ('line -> while line','line',2,'p_program','SyntacticAnalizer.py',53),
  ('line -> if line','line',2,'p_program','SyntacticAnalizer.py',54),
  ('line -> let line','line',2,'p_program','SyntacticAnalizer.py',55),
  ('line -> move line','line',2,'p_program','SyntacticAnalizer.py',56),
  ('line -> moveList line','line',2,'p_program','SyntacticAnalizer.py',57),
  ('line -> delay line','line',2,'p_program','SyntacticAnalizer.py',58),
  ('line -> println line','line',2,'p_program','SyntacticAnalizer.py',59),
  ('line -> break line','line',2,'p_program','SyntacticAnalizer.py',60),
  ('line -> empty empty','line',2,'p_program','SyntacticAnalizer.py',61),
  ('procedure -> FN ID LPAREN params RPAREN prodbody','procedure',6,'p_procedure','SyntacticAnalizer.py',74),
  ('prodbody -> LCRLBRACKET line RCRLBRACKET','prodbody',3,'p_prodbody','SyntacticAnalizer.py',79),
  ('function -> FN ID LPAREN params RPAREN funbody','function',6,'p_function','SyntacticAnalizer.py',90),
  ('params -> ID arg','params',2,'p_params','SyntacticAnalizer.py',95),
  ('params -> empty empty','params',2,'p_params','SyntacticAnalizer.py',96),
  ('arg -> COMMA params','arg',2,'p_arg','SyntacticAnalizer.py',107),
  ('arg -> COMMA arg','arg',2,'p_arg','SyntacticAnalizer.py',108),
  ('arg -> empty empty','arg',2,'p_arg','SyntacticAnalizer.py',109),
  ('funbody -> ARROW output LCRLBRACKET line end RCRLBRACKET','funbody',6,'p_funbody','SyntacticAnalizer.py',116),
  ('output -> INTEGER','output',1,'p_output','SyntacticAnalizer.py',122),
  ('output -> BOOLEAN','output',1,'p_output','SyntacticAnalizer.py',123),
  ('end -> RETURN expression SEMICOLON','end',3,'p_end','SyntacticAnalizer.py',129),
  ('loop -> LOOP LCRLBRACKET line RCRLBRACKET','loop',4,'p_loop','SyntacticAnalizer.py',140),
  ('for -> FOR ID IN INT DOTDOT INT LCRLBRACKET line RCRLBRACKET','for',9,'p_for','SyntacticAnalizer.py',155),
  ('while -> WHILE LPAREN expression compare expression RPAREN LCRLBRACKET line RCRLBRACKET','while',9,'p_while','SyntacticAnalizer.py',170),
  ('while -> WHILE TRUE LCRLBRACKET line RCRLBRACKET','while',5,'p_while','SyntacticAnalizer.py',171),
  ('move -> MOVE LPAREN STRING COMMA bool RPAREN SEMICOLON','move',7,'p_move','SyntacticAnalizer.py',186),
  ('moveList -> MOVE LPAREN LSQRBRACKET fingerList RSQRBRACKET COMMA bool RPAREN SEMICOLON','moveList',9,'p_moveList','SyntacticAnalizer.py',194),
  ('fingerList -> STRING COMMA STRING','fingerList',3,'p_fingerList','SyntacticAnalizer.py',202),
  ('fingerList -> STRING COMMA fingerList','fingerList',3,'p_fingerList','SyntacticAnalizer.py',203),
  ('delay -> DELAY LPAREN INT COMMA STRING RPAREN SEMICOLON','delay',7,'p_delay','SyntacticAnalizer.py',217),
  ('unit -> QUOT MIN QUOT','unit',3,'p_unit','SyntacticAnalizer.py',225),
  ('unit -> QUOT MIL QUOT','unit',3,'p_unit','SyntacticAnalizer.py',226),
  ('unit -> QUOT SEG QUOT','unit',3,'p_unit','SyntacticAnalizer.py',227),
  ('println -> PRINT EXPR LPAREN args RPAREN SEMICOLON','println',6,'p_println','SyntacticAnalizer.py',241),
  ('args -> INT body','args',2,'p_args','SyntacticAnalizer.py',253),
  ('args -> ID body','args',2,'p_args','SyntacticAnalizer.py',254),
  ('args -> opera body','args',2,'p_args','SyntacticAnalizer.py',255),
  ('args -> TRUE body','args',2,'p_args','SyntacticAnalizer.py',256),
  ('args -> FALSE body','args',2,'p_args','SyntacticAnalizer.py',257),
  ('args -> STRING body','args',2,'p_args','SyntacticAnalizer.py',258),
  ('body -> COMMA args','body',2,'p_body','SyntacticAnalizer.py',268),
  ('body -> COMMA body','body',2,'p_body','SyntacticAnalizer.py',269),
  ('body -> empty empty','body',2,'p_body','SyntacticAnalizer.py',270),
  ('text -> QUOT ID QUOT','text',3,'p_text','SyntacticAnalizer.py',277),
  ('elseiforelse -> elseif','elseiforelse',1,'p_elseiforelse','SyntacticAnalizer.py',289),
  ('elseiforelse -> else','elseiforelse',1,'p_elseiforelse','SyntacticAnalizer.py',290),
  ('if -> IF expression compare expression LCRLBRACKET line RCRLBRACKET empty','if',8,'p_if','SyntacticAnalizer.py',296),
  ('if -> IF expression compare expression LCRLBRACKET line RCRLBRACKET elseiforelse','if',8,'p_if','SyntacticAnalizer.py',297),
  ('elseif -> ELSEIF expression compare expression LCRLBRACKET line RCRLBRACKET empty','elseif',8,'p_elseif','SyntacticAnalizer.py',312),
  ('elseif -> ELSEIF expression compare expression LCRLBRACKET line RCRLBRACKET elseiforelse','elseif',8,'p_elseif','SyntacticAnalizer.py',313),
  ('else -> ELSE LCRLBRACKET line RCRLBRACKET','else',4,'p_else','SyntacticAnalizer.py',325),
  ('compare -> EQEQ','compare',1,'p_compare','SyntacticAnalizer.py',332),
  ('compare -> LTE','compare',1,'p_compare','SyntacticAnalizer.py',333),
  ('compare -> GTE','compare',1,'p_compare','SyntacticAnalizer.py',334),
  ('compare -> LT','compare',1,'p_compare','SyntacticAnalizer.py',335),
  ('compare -> GT','compare',1,'p_compare','SyntacticAnalizer.py',336),
  ('expression -> INT','expression',1,'p_expressions','SyntacticAnalizer.py',342),
  ('expression -> TRUE','expression',1,'p_expressions','SyntacticAnalizer.py',343),
  ('expression -> FALSE','expression',1,'p_expressions','SyntacticAnalizer.py',344),
  ('expression -> opera','expression',1,'p_expressions','SyntacticAnalizer.py',345),
  ('expression -> ID','expression',1,'p_expressions','SyntacticAnalizer.py',346),
  ('expression -> negative','expression',1,'p_expressions','SyntacticAnalizer.py',347),
  ('let -> LET ID ASSIGN operand SEMICOLON','let',5,'p_let','SyntacticAnalizer.py',360),
  ('let -> LET ID ASSIGN bool SEMICOLON','let',5,'p_let','SyntacticAnalizer.py',361),
  ('opera -> OPERA LPAREN operator COMMA operand COMMA operand RPAREN','opera',8,'p_opera','SyntacticAnalizer.py',377),
  ('operator -> PLUS','operator',1,'p_operators','SyntacticAnalizer.py',385),
  ('operator -> MINUS','operator',1,'p_operators','SyntacticAnalizer.py',386),
  ('operator -> DIVIDE','operator',1,'p_operators','SyntacticAnalizer.py',387),
  ('operator -> ASTR','operator',1,'p_operators','SyntacticAnalizer.py',388),
  ('operator -> TIMES','operator',1,'p_operators','SyntacticAnalizer.py',389),
  ('operand -> INT','operand',1,'p_operand','SyntacticAnalizer.py',396),
  ('operand -> opera','operand',1,'p_operand','SyntacticAnalizer.py',397),
  ('operand -> ID','operand',1,'p_operand','SyntacticAnalizer.py',398),
  ('operand -> negative','operand',1,'p_operand','SyntacticAnalizer.py',399),
  ('negative -> MINUS INT','negative',2,'p_uminus','SyntacticAnalizer.py',405),
  ('bool -> TRUE','bool',1,'p_expression_bool','SyntacticAnalizer.py',411),
  ('bool -> FALSE','bool',1,'p_expression_bool','SyntacticAnalizer.py',412),
  ('bool -> ID','bool',1,'p_expression_bool','SyntacticAnalizer.py',413),
  ('break -> BREAK','break',1,'p_break','SyntacticAnalizer.py',420),
  ('empty -> <empty>','empty',0,'p_empty','SyntacticAnalizer.py',437),
]
