# reelay

`reelay` generates some `C++` code that matches the regular expression given.

# install

This package requires `python3` and  `antlr4-python3-runtime`.

The easiest way to install `reelay` is to run the following command. 

    pip install git+https://github.com/doganulus/reelay.git

# usage

reelay [-h] [--with-re2] PATTERN

Pattern Syntax:     
  
    Expr = a                   (Letter)
         : Expr1 | Expr2       (Union)
         : Expr1 ; Expr2       (Concatenation)
         : Expr1 *             (Zero-or-more Repetition)
         : Expr1 +             (One-or-more Repetition)
         : Expr1 ?             (Zero-or-one Repetition)

Optional Arguments:

    -h, --help  show this help message and exit
    --with-re2  generate equivalent code using Google's RE2 to match
