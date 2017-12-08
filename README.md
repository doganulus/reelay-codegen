# reelay

reelay generates some C++ code that matches the regular expression given

# usage

reelay [-h] [--with-re2] pattern

positional arguments:
  pattern     Expr = a                   (Letter)
                   : Expr1 | Expr2       (Union)
                   : Expr1 ; Expr2       (Concatenation)
                   : Expr1 *             (Zero-or-more Repetition)
                   : Expr1 +             (One-or-more Repetition)
                   : Expr1 ?             (Zero-or-one Repetition)

optional arguments:
  -h, --help  show this help message and exit
  --with-re2  generate equivalent code using Google's RE2 to match
