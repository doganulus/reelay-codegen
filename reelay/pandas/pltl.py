import numpy as np
import pandas as pd

from antlr4 import *

from reelay.parser.PastLTLLexer import PastLTLLexer
from reelay.parser.PastLTLParser import PastLTLParser
from reelay.parser.PastLTLVisitor import PastLTLVisitor

def eval(df, expr, inplace=False, local_dict=dict(), global_dict=dict()):
    "Compile a past linear-time temporal logic formula, and evaluate."

    lexer = PastLTLLexer(InputStream(expr))
    stream = CommonTokenStream(lexer)
    parser = PastLTLParser(stream)
    tree = parser.namedExpr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    builder = PastLTLBuilder()
    builder.run(tree)

    code = '\n'.join(builder.statements)
    machine = compile(code, "<string>", "exec")

    print(code)

    states = np.array(builder.initialization)
    def output(machine, _step):     
        exec(machine, globals(), {**local_dict, **locals()})
        yield states[-1]


    data = (output(machine, _step) for _step in df.itertuples())
    new_frame = pd.DataFrame(columns=[builder.name], data=data)

    if inplace:
        df[builder.name] = new_frame
        return df
    else:
        return new_frame
    

class PastLTLBuilder(PastLTLVisitor):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.name = None
        self.initialization = list()
        self.statements = list()

    def run(self, tree):
        child = self.visit(tree)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = {};".format(label, child))
        self.num = self.num + 1 

        return self.initialization, self.statements

    # def visitAtomic(self, ctx:PastLTLParser.AtomicContext):
    #     name = ctx.child.getText()
    #     return "_step.{}".format(name)

    def visitNamedExpr(self, ctx:PastLTLParser.NamedExprContext):
        try:
            ctx.name = ctx.name.text
        except AttributeError as e:
            ctx.name = None

        return self.visit(ctx.child)

    def visitProp(self, ctx:PastLTLParser.PropContext):
        name = ctx.name.text
        return "_step.{}".format(name)

    def visitPred(self, ctx:PastLTLParser.PredContext):
        name = ctx.name.text
        args = ctx.args.getText().split(',')
        nargs = ["_step.{}".format(arg) for arg in args] 

        # return "_step.{}".format(name)
        return "{name}({params})".format(name=name, params=','.join(nargs))

    # def visitIdlist(self, ctx:PastLTLParser.IdlistContext):
    #     l = list()

    #     return l

    def visitNegation(self, ctx:PastLTLParser.NegationContext):
        child = self.visit(ctx.child)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = not {};".format(label, child))
        self.num = self.num + 1 

        return label

    def visitDisjunction(self, ctx:PastLTLParser.DisjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = {} or {};".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitConjunction(self, ctx:PastLTLParser.ConjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = {} and {};".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitSince(self, ctx:PastLTLParser.SinceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{label} = {right} or ({label} and {left});".format(label=label, left=left, right=right))
        self.num = self.num + 1 

        return label

    def visitAlways(self, ctx:PastLTLParser.AlwaysContext):
        child = self.visit(ctx.child)
        label = "states[{}]".format(self.num)

        self.initialization.append(True)
        self.statements.append("{label} = {label} and {child};".format(label=label, child=child))
        self.num = self.num + 1 

        return label

    def visitOnce(self, ctx:PastLTLParser.OnceContext):
        child = self.visit(ctx.child)
        label = "states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{label} = {label} or {child};".format(label=label, child=child))
        self.num = self.num + 1 

        return label

    # Visit a parse tree produced by PastLTLParser#Grouping.
    def visitGrouping(self, ctx:PastLTLParser.GroupingContext):
        return self.visit(ctx.child)

