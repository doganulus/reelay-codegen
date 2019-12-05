from reelay.machine.common import *

class PreviousUpdate(Expr):
    """docstring for Atomic"""
    def __init__(self, state, child):
        super().__init__()
        self.children = [Pre(state), child]

class OnceUpdate(Expr):
    """docstring for Atomic"""
    def __init__(self, state, child):
        super().__init__()
        self.children = [Pre(state), child]

class AlwaysUpdate(Expr):
    """docstring for Atomic"""
    def __init__(self, state, child):
        super().__init__()
        self.children = [Pre(state), child]

class SinceUpdate(Expr):
    """docstring for Atomic"""
    def __init__(self, state, left, right):
        super().__init__()
        self.children = [Pre(state), left, right]

class PreviousOutput(Expr):
    """docstring for Atomic"""
    def __init__(self, state):
        super().__init__()
        self.children = [Pre(state)]

class TemporalOutput(Expr):
    """docstring for Atomic"""
    def __init__(self, state):
        super().__init__()
        self.children = [state]

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
