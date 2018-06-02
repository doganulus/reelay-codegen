from reelay.machine.common import Expr

class TimedSetUnion(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children

class TimedSetIntersection(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children

class TimedSetComplementation(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children

class TimedSetSinceUpdate(Expr):
    """docstring for Atomic"""
    def __init__(self, state, left, right, lower_bound=None, upper_bound=None):
        super().__init__()
        self.children = [state, left, right]
        self.l = lower_bound
        self.u = upper_bound

class TimedSetSinceOutput(Expr):
    """docstring for Atomic"""
    def __init__(self, state, lower_bound=None, upper_bound=None):
        super().__init__()
        self.children = [state]
        self.l = lower_bound
        self.u = upper_bound

class TimedSetConstant(Expr):
    """docstring for Atomic"""
    def __init__(self, *children):
        super().__init__()
        self.children = children

class TimedSetState(object):
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
