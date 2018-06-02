
class Expr(object):
    """docstring for Expr"""
    def __init__(self):
        super().__init__()
        self.children = []

# class Atom(object):
#     """docstring for Atom"""
#     def __init__(self, name, dtype=None, args=[], nullable=False):
#         super().__init__()
#         self.name = name
#         self.dtype = dtype
#         self.args = args
#         self.output = self

# class Or(Expr):
#     """docstring for Atomic"""
#     def __init__(self, *children):
#         super().__init__()
#         self.children = children
#         self.reduce()

#     def reduce(self):
#         self.children = list(set(flatten([c.children if isinstance(c, Or) else c for c in self.children])))

# class And(Expr):
#     """docstring for Atomic"""

#     def __init__(self, *children):
#         super().__init__()
#         self.children = children
#         self.reduce()

#     def reduce(self):
#         self.children = list(set(flatten([c.children if isinstance(c, And) else c for c in self.children])))

# class Not(Expr):
#     def __new__(cls, child):
#         if isinstance(child, Not):
#             return child.children[0]
#         else:
#             return super(Not, cls).__new__(cls)

#     def __init__(self, child):
#         super().__init__()
#         self.children = [child]

class Constant(object):
    def __init__(self, name):
        self.name = name

# class True(Constant):
#     def __init__(self):
#         self.name = 'true'

# class False(Constant):
#     def __init__(self):
#         self.name = 'false'

class Now(object):
    """docstring for Machine"""

    def __init__(self, state):
        super().__init__()
        self.state = state

class Pre(object):
    """docstring for Machine"""

    def __init__(self, state):
        super().__init__()
        self.state = state


def flatten(l): 
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

