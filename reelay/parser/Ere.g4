grammar Ere;

expr : child=atom               # Atomic
     | 'exists' variables=idlist '.' child=expr           # Exists
     | '~' child=expr           # Complement
     | left=expr '{' min_val=NUMBER ',' max_val=NUMBER '}' # Restrict
     | left=expr '&' right=expr # Intersect           
     | child=expr '*'           # Star
     | child=expr '+'           # Plus
     | child=expr '?'           # Question
     | left=expr ';' right=expr # Concat
     | left=expr '|' right=expr # Union       
     | '(' child=expr ')'       # Grouping    
     ;

atom : IDENTIFIER;
idlist : IDENTIFIER (',' IDENTIFIER)* ;

//formlist : form (',' form)* ;
//form: IDENTIFIER 
//  | IDENTIFIER '=' IDENTIFIER
//  ;



IDENTIFIER : [_a-zA-Z][_a-zA-Z0-9]*;

NUMBER: DIGIT | (DIGIT_NOT_ZERO DIGIT+);

WS         : [ \r\n\t]+ -> channel (HIDDEN);

fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');
