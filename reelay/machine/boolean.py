from reelay.machine.common import *

class BooleanOr(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children
        self.reduce()

    def reduce(self):
        self.children = list(set(flatten([c.children if isinstance(c, BooleanOr) else c for c in self.children])))

class BooleanAnd(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children
        self.reduce()

    def reduce(self):
        self.children = list(set(flatten([c.children if isinstance(c, BooleanAnd) else c for c in self.children])))

class BooleanNot(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children


class BooleanState(object):
    """docstring for Machine"""

    def __init__(self, update, init=False, output=None, variable=None):
        super().__init__()

        self.init = init
        self.update = update
        self.variable = variable

        if output != None:
            self.output = output
        else:
            self.output = self

