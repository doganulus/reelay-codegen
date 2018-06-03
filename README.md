# reelay

`reelay` is a `C++` code generator for monitoring, inspecting, and analyzing sequential data in an online fashion. `reelay` allows developers to monitor high-level (formal) patterns for their applications without being an expert in the theory. `reelay` supports several pattern specification languages (variants of regular expressions and temporal logic) and its potential applications include real-time data analytics and robotics.

# install

This package requires `python3` and `antlr4-python3-runtime`.

The easiest way to install `reelay` is to run the following command (that requires `git` installed in your system). 

    pip install git+https://github.com/doganulus/reelay.git

# usage

`reelay` has a command-line script `reelay` to generate a `C++` class that corresponds to the specification.

reelay [-h] [--reg] [--tl] [--with-headers] PATTERN

Optional Arguments:

    -h              show the help message
    --reg           generate code from regular expression pattern
    --tl            generate code from temporal logic pattern
    --with-headers  generate code with required headers





