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
     | 'once' '[' '>=' l=CONSTANT ']' child=expr                    # TimedOnceGT
     | 'once' '[' '<=' u=CONSTANT ']' child=expr                    # TimedOnceLT
     | 'once' '[' l=CONSTANT ',' u=CONSTANT ']' child=expr           # TimedOnce
     | 'always' child=expr                                          # Always
     | 'always' '[' '>=' l=CONSTANT ']' child=expr                # TimedAlwaysGT
     | 'always' '[' '<=' u=CONSTANT ']' child=expr                # TimedAlwaysLT
     | 'always' '[' l=CONSTANT ',' u=CONSTANT ']' child=expr      # TimedAlways
     | left=expr 'since' right=expr                                 # Since     
     | left=expr 'since' '[' '>=' l=CONSTANT ']' right=expr        # TimedSinceGT
     | left=expr 'since' '[' '<=' u=CONSTANT ']' right=expr        # TimedSinceLT
     | left=expr 'since' '[' l=CONSTANT ',' u=CONSTANT ']' right=expr #TimedSince
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

TYPEDVAR : IDENTIFIER ':' ('bool' | 'int' | 'float' | 'double' | 'string'); 


CONSTANT
    :   NATURAL
    |   FLOATING
    ;

fragment
NATURAL
    :   DIGIT_NOT_ZERO DIGIT*
    ;

fragment
FLOATING
    :   FRACTIONALCONSTANT EXPONENTPART?
    |   DIGITSEQUENCE EXPONENTPART 
    ;

fragment
FRACTIONALCONSTANT
    :   DIGITSEQUENCE? '.' DIGITSEQUENCE
    |   DIGITSEQUENCE '.'
    ;

fragment
EXPONENTPART
    :   'e' SIGN? DIGITSEQUENCE
    |   'E' SIGN? DIGITSEQUENCE
    ;

fragment SIGN : '+' | '-';
fragment DIGITSEQUENCE : DIGIT+;
fragment DIGIT : ('0'..'9');
fragment DIGIT_NOT_ZERO : ('1'..'9');

WS: [ \r\n\t]+ -> channel (HIDDEN);
