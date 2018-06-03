Temporal Logic Syntax:     
  
    Expr == Atom                    (Atomic Expression)

         :: Expr1 *                 (Negation)
         :: Expr1 || Expr2          (Disjunction)
         :: Expr1 && Expr2          (Conjunction)
         :: Expr1 -> Expr2          (Implies)
         
         :: Pre Expr                (Previously operator)
        
         :: once Expr               (Once operator)
         :: once[a,b] Expr          (Time bounded Once operator by [a,b])
         :: once[<=b] Expr          (Time bounded Once operator by [0,b])
         :: once[>=a] Expr          (Time bounded Once operator by [a,Inf))

         :: always Expr             (Always in the past operator)
         :: always[a,b] Expr        (Time bounded Always operator by [a,b])
         :: always[<=b] Expr        (Time bounded Always operator by [0,b])
         :: always[>=a] Expr        (Time bounded Always operator by [a,Inf))
         
         :: Expr1 since Expr2       (Since operator)
         :: Expr1 since[a,b] Expr2  (Time bounded Since operator by [a,b])
         :: Expr1 since[<=b] Expr2  (Time bounded Since operator by [0,b])
         :: Expr1 since[>=a] Expr2  (Time bounded Since operator by [a,Inf))

         :: (Expr)                  (Grouping)

    Atom == PropName                (Proposition)
         :: FuncName(Arg1,...,Argn) (Predicate / Boolean valued function)

    Arg  == ArgName                 (Boolean argument)
         == ArgName : ArgType       (Other typed argument)
