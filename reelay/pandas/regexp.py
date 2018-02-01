import numpy as np
import pandas as pd

from antlr4 import *

from reelay.parser.RegExpLexer import RegExpLexer
from reelay.parser.RegExpParser import RegExpParser
from reelay.parser.RegExpVisitor import RegExpVisitor

def eval(df, expr, inplace=False, local_dict=dict(), global_dict=dict()):
    "Compile a regular expression, and evaluate."

    lexer = RegExpLexer(InputStream(expr))
    stream = CommonTokenStream(lexer)
    parser = RegExpParser(stream)
    tree = parser.namedExpr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    builder = RegBuilder()
    initialization, statements = builder.run(tree)


    code = '\n'.join(statements)
    machine = compile(code, "<string>", "exec")

    # print(code)

    states = np.array(initialization)
    nstates = np.array(initialization)
    output = np.array([False])

    data = []
    for letter in df.itertuples():
        exec(machine, globals(), {**local_dict, **locals()})
        states = np.copy(nstates)
        data.append(output[0])
    
    new_frame = pd.DataFrame(columns=[builder.name], data=data)

    if inplace:
        df[builder.name] = new_frame
        return df
    else:
        return new_frame

class RegBuilder(object):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.name = None
        self.initialization = [True]
        self.statements = list()

    def run(self, tree):

        annotator = RegAnnotator()
        size, nullable, output = annotator.walk(tree)

        architect = RegArchitect()
        trigger = architect.walk(tree, set([0]))

        self.name = tree.name 
        self.initialization.extend([False] * (size-1))
        
        self.statements.append('nstates[0] = 1;')

        for position, flag, trigger in trigger:
            trig_cond = ' or '.join(['states[{}]'.format(i) for i in trigger])
            self.statements.append('nstates[{}] = {} and ({});'.format(position, flag, trig_cond))
            # trig_cond = ', slyvan_or('.join(['next_state[{}]'.format(i) for i in trigger])
            # statements.append('\t\tnext_state[{}] = (letter == \'{}\') and slyvan_or({}, sylvan_bdd_false{};'.format(position, letter, trig_cond, ')'*len(trigger) ))

        self.statements.append('states = np.copy(nstates);')

        self.statements.append('output[0] = ' + ' or '.join(['nstates[{}]'.format(i) for i in output]) + ';')

        return self.initialization, self.statements


    
class RegAnnotator(RegExpVisitor):

    def __init__(self):
        super().__init__()
        self.num = 1

    def walk(self, tree):
        return self.visit(tree)

    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        try:
            ctx.name = ctx.name.text
        except AttributeError as e:
            ctx.name = None
        return self.visit(ctx.child)

    def visitPred(self, ctx:RegExpParser.PredContext):
        name = ctx.name.text
        nargs = ["letter.{}".format(arg) for arg in ctx.args.getText().split(',')]

        ctx.callname = "{name}({params})".format(name=name, params=','.join(nargs))

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num

        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Atomic.
    def visitProp(self, ctx:RegExpParser.PropContext):

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num
        ctx.callname = 'letter.{}'.format(ctx.name.text)
        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitAtomic(self, ctx:RegExpParser.AtomicContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    def visitUnion(self, ctx:RegExpParser.UnionContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable or ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):

        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable and ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output if ctx.right.nullable else ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable 
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

class RegArchitect(RegExpVisitor):

    def __init__(self):
        super().__init__()

    def walk(self, tree, trigger=set([0])):
        tree.trigger = trigger
        return self.visit(tree)

    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        return self.walk(ctx.child, ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Atomic.
    def visitAtomic(self, ctx:RegExpParser.AtomicContext):
        return self.walk(ctx.child, ctx.trigger)

    def visitProp(self, ctx:RegExpParser.PropContext):
        return [(ctx.position, ctx.callname, ctx.trigger)]

    def visitPred(self, ctx:RegExpParser.PredContext):
        return [(ctx.position, ctx.callname, ctx.trigger)]

    def visitUnion(self, ctx:RegExpParser.UnionContext):
        left = self.walk(ctx.left, ctx.trigger)
        right = self.walk(ctx.right, ctx.trigger)

        return left + right

    # Visit a parse tree produced by RegExpParser#Concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):

        left = self.walk(ctx.left, ctx.trigger)

        if ctx.left.nullable:
            right = self.walk(ctx.right, ctx.left.output | ctx.trigger)
        else:
            right = self.walk(ctx.right, ctx.left.output)

        return left + right

    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):
        return self.walk(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):
        return self.walk(ctx.child, ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):
        return self.walk(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):
        return self.walk(ctx.child, ctx.child.output | ctx.trigger)

