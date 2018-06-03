# reelay

`reelay` is a `C++` code generator for monitoring, pattern matching, and analyzing temporal data streams on-the-fly. `reelay` allows developers to monitor high-level (formal) patterns for their applications in an efficient and effortless way. `reelay` supports several popular pattern specification languages, namely regular expressions, temporal logic, and their variants. Potential application areas include real-time data analytics and robotics.

# install

`reelay` requires `python3` and `antlr4-python3-runtime` for code generation.

The easiest way to install `reelay` is to run the following command (that requires `git` installed in your system). 

    pip install git+https://github.com/doganulus/reelay.git

# usage

`reelay` has a command-line script `reelay` to generate a `C++` class that corresponds to the specification.

reelay [-h] [--re] [--tl] [--with-headers] PATTERN

Optional Arguments:

    -h              show the help message
    --re            generate code from regular expression pattern
    --tl            generate code from temporal logic pattern
    --with-headers  generate code with required headers





