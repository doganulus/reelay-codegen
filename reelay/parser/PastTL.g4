grammar PastTL;

namedExpr : (name=IDENTIFIER '=')? child=expr;

expr : child=binded_atom                                            # Atomic
     | 'exists' '{' args=idlist '}' child=expr                      # Exists
     | ('!' | 'not') child=expr                                     # Negation
     | left=expr ('&&' | 'and') right=expr                          # Conjunction
     | left=expr ('||' | 'or') right=expr                           # Disjunction
     | left=expr ('->' | 'implies') right=expr                      # Implication
     | 'pre' child=expr                                             # Previous
     | 'once' child=expr                                            # Once
     | 'once' '[' '>=' l=NATURAL ']' child=expr                    # TimedOnceGT
     | 'once' '[' '<=' u=NATURAL ']' child=expr                    # TimedOnceLT
     | 'once' '[' l=NATURAL ',' u=NATURAL ']' child=expr           # TimedOnce
     | 'always' child=expr                                          # Always
     | 'always' '[' '>=' l=NATURAL ']' child=expr                # TimedAlwaysGT
     | 'always' '[' '<=' u=NATURAL ']' child=expr                # TimedAlwaysLT
     | 'always' '[' l=NATURAL ',' u=NATURAL ']' child=expr      # TimedAlways
     | left=expr 'since' right=expr                                 # Since     
     | left=expr 'since' '[' '>=' l=NATURAL ']' right=expr        # TimedSinceGT
     | left=expr 'since' '[' '<=' u=NATURAL ']' right=expr        # TimedSinceLT
     | left=expr 'since' '[' l=NATURAL ',' u=NATURAL ']' right=expr #TimedSince
     | '(' child=expr ')'                                           # Grouping
     ;

binded_atom : child=atom                         # VarConst
            | varname=IDENTIFIER '<=' child=atom # VarBind
            ;

atom : name=(TYPEDVAR | IDENTIFIER)                    # Prop
     | name=(TYPEDVAR | IDENTIFIER) '(' args=alist ')' # Pred
     | CONSTANT                                        # Constant
     ;

alist : atom (',' atom)*                # AtomList
      ;

idlist : IDENTIFIER (',' IDENTIFIER)*;

IDENTIFIER : [a-zA-Z][_a-zA-Z0-9]*;

TYPEDVAR : IDENTIFIER ':' ('bool' | 'int' | 'int32' |  'float' | 'float64' | 'double' | 'string' ); 

CONSTANT : SIGN? NATURAL | SIGN? FLOATING; 

NATURAL
    :   DIGITS
    ;

FLOATING
    :   FRACTIONALCONSTANT EXPONENTPART?
    |   DIGITS EXPONENTPART 
    ;

fragment
FRACTIONALCONSTANT
    :   DIGITS? '.' DIGITS
    |   DIGITS '.'
    ;

fragment
EXPONENTPART
    :   'e' SIGN? DIGITS
    |   'E' SIGN? DIGITS
    ;

fragment SIGN : '+' | '-';
fragment DIGITS : DIGIT+;
fragment DIGIT : ('0'..'9');

WS: [ \r\n\t]+ -> channel (HIDDEN);
