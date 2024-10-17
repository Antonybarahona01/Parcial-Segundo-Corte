grammar fourier;

prog:   start+ ;

start: function NEWLINE ;

function: 'f(' ( VAR | VAR '/' VARN ) ')' '=' '{' parameters '}'  #Recta
        | 'f(' ( VAR | VAR '/' VARN ) ')' '=' '{' parameters1 '}' #Triang
        | 'sign('  VAR  ')' '=' '{' parameters2 '}'               #Sign
        | 'u('  VAR  ')' '=' '{' parameters3 '}'                  #U
        | 'd('  VAR  ')'                                          #D
        | 'cos(' (VARN ('+' | '-' | '*' | '/')?)?  VAR  ')'                                      #Cos
        | 'sin(' (VARN ('+' | '-' | '*' | '/')?)?  VAR  ')'                                      #Sin
        | 'SUM( inf, n = -inf , d(' VAR  '-n' VARN '))'           #Sum
        ;

parameters: '(' inr ')' ',' '(' inr ')'  ( ',' '(' inr ')' )? ;
parameters1: '(' inr2 ')' ',' '(' inr2 ')'  ( ',' '(' inr2 ')' )? ;
parameters2: '(' inr3 ')' ',' '(' inr4 ')' ;
parameters3: '(' inr3 ')' ',' '(' inr5 ')' ;

inr: ('0' | '1')  ',' ( INT1 comp_operator )? VAR comp_operator INT1 ;
inr2: ('0' | '1') ('-'  VAR | VAR '/' VARN )? ',' ( INT comp_operator )? VAR comp_operator VARN ;
inr3: '1'  ','  VAR '>' '0' ;
inr4: '-1'  ','  VAR '<' '0' ;
inr5: '0'  ','  VAR '<' '0' ;

// Lexer rules
comp_operator:  '<' | '<=' | '>' | '>=';
INT1 : VARN '/2' ;
VAR: [a-zA-Z] ;
VARN : [a-zA-Z] | INT ;
ID: [a-zA-Z]+ ;
RECT: 'rect';
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
NEWLINE:'\r'? '\n' ;     
WS  :   [ \t]+ -> skip ; 
