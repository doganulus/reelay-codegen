# reelay

`reelay` generates some `C++` code that matches the regular expression given.

# install

This package requires `python3` and  `antlr4-python3-runtime`.

The easiest way to install `reelay` is to run the following command (that requires `git` installed in your system). 

    pip install git+https://github.com/doganulus/reelay.git

# usage

`reelay` is a Python package but includes a command-line utility of the same name.

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

# example

The installation will provide a command-line script. Then we execute `reelay` for a user-provided regular expression as follows:

    reelay '(((a;b)|b)*);b;a'

It generates a simple `C++` program called `matcher-reelay.cpp` to be compiled any `C++`. For example,

    g++ -O2 -o matcher-reelay matcher-reelay.cpp

Now we can check whether a string (given in a file) matches the regular expression.

    ./matcher-reelay textfile.txt

The option `--with-re2` would generate similar `matcher-re2.cpp` and `matcher-re2-nfa.cpp` programs that uses Google's RE2 engine for comparison purposes.

There are still rough edges inside such as the memory trick to force RE2 to generate an NFA. Be aware :)