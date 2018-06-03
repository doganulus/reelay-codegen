Regular Expression Syntax:     
  
    Expr == Atom                    (Atomic Expression)
         :: Expr1 | Expr2           (Union)
         :: Expr1 ; Expr2           (Concatenation)
         :: Expr1 *                 (Zero-or-more Repetition)
         :: Expr1 +                 (One-or-more Repetition)
         :: Expr1 ?                 (Zero-or-one Repetition)
         :: (Expr)                  (Grouping)

    Atom == PropName                (Proposition)
         :: FuncName(Arg1,...,Argn) (Predicate / Boolean valued function)

    Arg  == ArgName                 (Boolean argument)
         :: ArgName : ArgType       (Other typed argument)

Example Patterns:
