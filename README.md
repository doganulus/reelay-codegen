# reelay

`reelay` is a `C++` code generator for monitoring, pattern matching, and analyzing temporal data streams on-the-fly. `reelay` allows developers to monitor high-level (formal) patterns for their applications in an efficient and effortless way. `reelay` supports several popular pattern specification languages, namely regular expressions, temporal logic, and their variants. Potential application areas include real-time data analytics and robotics.

# install

`reelay` requires `python3` and `antlr4-python3-runtime` for code generation.

The easiest way to install `reelay` is to run the following command (that requires `git` installed in your system). 

    pip install git+https://github.com/doganulus/reelay.git

Additionally compiling generated code additionally requires `boost` software libraries installed on your system.

# usage

`reelay` provides two command-line scripts, `re2cpp` and `tl2cpp` to generate `C++` classes that correspond to regular expression and temporal logic PATTERNs, respectively. 

    re2cpp [-h] [--with-headers] PATTERN  
    tl2cpp [-h] [--with-headers] PATTERN
     
    Optional Arguments:
     
    -h              show the help message
    --outdir        specify a directory for generated files
    --with-headers  generate code with required headers

[Syntax reference for regular expressions](http://) 
[Syntax reference for temporal logic formulas](http://) 

# getting started

`reelay` is designed to process sequences of data tuples (messages) in an online fashion. For example, consider a sequence of two concurrent Boolean variables `p1` and `p2`. 

         1 2 3 4 5 6 7 8 9 
    p1 : 0 1 0 0 0 0 1 1 0
    p2 : 0 0 1 1 1 1 0 0 0 

Then we want to detect a pattern such that `p2` is continuously true (`1`) between two instants where `p1` is true (`1`). The corresponding regular expression is below.
    
    Expr = p1;p2+;p1

When a suffix of the sequence matches the pattern, the output `y` would be computed by the monitor as follows.

         1 2 3 4 5 6 7 8 9 
    p1 : 0 1 0 0 0 0 1 1 0
    p2 : 0 0 1 1 1 1 0 0 0 
     y : 0 0 0 0 0 0 1 0 0

It is possible to extend monitoring towards numerical and mixed-type data sequences. We provide support for arbitrary predicates (given by user as `C++` functions) and basic types for variables. 

    Expr = lt(x1:double, 3.4) ; gt(x2:int, 7)+ ; p3

         1   2   3 4 5     6 7 8 9 
    x1 : 1.1 4.3 1.5 5.5 5.6  6.0 6.0 6.0 6.0
    x2 : 2   3   6   8   44   12  10  0   0
    p3 : 0   0   1   0   0    0   0   1   0 
     y : 0   0   0   0   0    0   0   1   0
 
Besides temporal logic provides additional operators to define patterns including operators with timing constraints.

# applications

`reelay` package includes two example applications to monitor (1) CSV files and (2) data streams of Robot Operating System (ROS). These applications can be found in `examples` folder.












