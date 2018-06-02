from antlr4 import *

from reelay.parser.PastTLLexer import PastTLLexer
from reelay.parser.PastTLParser import PastTLParser
from reelay.parser.PastTLVisitor import PastTLVisitor

from reelay.machine.common import *
from reelay.machine.boolean import *
from reelay.machine.timed import *


class PastTLBuilder(PastTLVisitor):

    def __init__(self):
        super().__init__()
        self.states = list()
        self.meta = dict(name='name', bnum=0, tnum=0, vars=set(), funcs=set())

    def build(self, expr):

        lexer = PastTLLexer(InputStream(expr))
        stream = CommonTokenStream(lexer)
        parser = PastTLParser(stream)
        tree = parser.namedExpr()

        self.meta['expr'] = expr

        child = self.visit(tree)

        return self.states, self.meta

    def visitNamedExpr(self, ctx:PastTLParser.NamedExprContext):

        child = self.visit(ctx.child)

        try:
            name = ctx.name.text
        except AttributeError as e:
            name = 'Expr'

        self.meta['name'] = name
        self.meta['output'] = child.output

        # state = BooleanState(
        #     update=child.output,
        #     variable=self.meta['bnum']
        #     )

        # self.meta['bnum'] += 1
        # self.states.append(state)

        return child

    def visitAtomList(self, ctx:PastTLParser.AtomListContext):
        uncomma = [child for child in ctx.children if child.getText() != ',']
        return [self.visit(child) for child in uncomma]

    def visitConstant(self, ctx:PastTLParser.ConstantContext):
        return Constant(ctx.getText())

    def visitProp(self, ctx:PastTLParser.PropContext):
        # definition = ctx.name.text
        try:
            name, dtype = ctx.name.text.split(':')
        except:
            name = ctx.name.text
            dtype = 'bool'

        self.meta['vars'] = self.meta['vars'] | set([(dtype, name)])
        return Atom(name, dtype)

    def visitPred(self, ctx:PastTLParser.PredContext):

        args = self.visit(ctx.args)

        try:
            name, dtype = ctx.name.text.split(':')
        except:
            name = ctx.name.text
            dtype = 'bool'
        # args = ','.join([str(atom) for atom in atoms])

        self.meta['funcs'] = self.meta['funcs'] | set([(dtype, name)])
        return Atom(name, dtype, args)

    def visitVarConst(self, ctx:PastTLParser.VarConstContext):
        return self.visit(ctx.child)

    def visitVarBind(self, ctx:PastTLParser.VarBindContext):
        raise NotImplementedError

    def visitExists(self, ctx:PastTLParser.ExistsContext):
        raise NotImplementedError

    def visitNegation(self, ctx:PastTLParser.NegationContext):
        child = self.visit(ctx.child)

        print(child)

        state = BooleanState(
            update=BooleanNot(child.output), 
            variable=self.meta['bnum']
            )
        self.meta['bnum'] += 1

        self.states.append(state)

        return state

    def visitDisjunction(self, ctx:PastTLParser.DisjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = BooleanState(
            update=BooleanOr(left.output, right.output), 
            variable=self.meta['bnum']
            )
        self.meta['bnum'] += 1

        self.states.append(state)

        return state

    def visitConjunction(self, ctx:PastTLParser.ConjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = BooleanState(
            update=BooleanAnd(left.output, right.output),
            variable=self.meta['bnum']
            )

        self.meta['bnum'] += 1
        self.states.append(state)

        return state

    def visitImplication(self, ctx:PastTLParser.ConjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = BooleanState(
            update=BooleanOr(BooleanNot(left.output), right.output),
            variable=self.meta['bnum']
            )

        self.meta['bnum'] += 1
        self.states.append(state)

        return state

    def visitPrevious(self, ctx:PastTLParser.PreviousContext):
        child = self.visit(ctx.child)

        state = BooleanState(
            update=child.output, 
            variable=self.meta['bnum']
            )
        state.output=Pre(state)

        self.meta['bnum'] += 1
        self.states.append(state)

        return state

    def visitSince(self, ctx:PastTLParser.SinceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = BooleanState(
            update=None,
            variable=self.meta['bnum']
            )
        state.update = BooleanOr(right.output, BooleanAnd(Pre(state.output), left.output))

        self.meta['bnum'] += 1
        self.states.append(state)

        return state

    def visitTimedSinceLT(self, ctx:PastTLParser.TimedSinceLTContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, left.output, right.output, None, int(ctx.u.text))
        state.output = TimedSetSinceOutput(state, None, int(ctx.u.text))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitTimedSinceGT(self, ctx:PastTLParser.TimedSinceGTContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, left.output, right.output, int(ctx.l.text), None)
        state.output = TimedSetSinceOutput(state, int(ctx.l.text), None)

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitTimedSince(self, ctx:PastTLParser.TimedSinceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, left.output, right.output, int(ctx.l.text), int(ctx.u.text))
        state.output = TimedSetSinceOutput(state, int(ctx.l.text), int(ctx.u.text))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitAlways(self, ctx:PastTLParser.AlwaysContext):
        child = self.visit(ctx.child)

        state = BooleanState(
            update=None,
            variable=self.meta['bnum']
            )
        state.update = BooleanAnd(Pre(state.output), child.output)

        self.meta['bnum'] += 1
        self.states.append(state)

        return state

    def visitTimedAlwaysLT(self, ctx:PastTLParser.TimedAlwaysLTContext):
        child = self.visit(ctx.child)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, Constant('true'), BooleanNot(child.output), None, int(ctx.u.text))
        state.output = BooleanNot(TimedSetSinceOutput(state, None, int(ctx.u.text)))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitTimedAlwaysGT(self, ctx:PastTLParser.TimedAlwaysGTContext):
        child = self.visit(ctx.child)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, Constant('true'), BooleanNot(child.output), int(ctx.l.text), None)
        state.output = BooleanNot(TimedSetSinceOutput(state, int(ctx.l.text), None))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitTimedAlways(self, ctx:PastTLParser.TimedAlwaysContext):
        child = self.visit(ctx.child)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, Constant('true'), BooleanNot(child.output), int(ctx.l.text), int(ctx.u.text))
        state.output = BooleanNot(TimedSetSinceOutput(state, int(ctx.l.text), int(ctx.u.text)))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitOnce(self, ctx:PastTLParser.OnceContext):
        child = self.visit(ctx.child)

        state = BooleanState(
            update=None,
            variable=self.meta['bnum']
            )
        state.update = BooleanOr(Pre(state.output), child.output)

        self.meta['bnum'] += 1
        self.states.append(state)

        return state

    def visitTimedOnceLT(self, ctx:PastTLParser.TimedOnceLTContext):
        child = self.visit(ctx.child)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, Constant('true'), child.output, None, int(ctx.u.text))
        state.output = TimedSetSinceOutput(state, None, int(ctx.u.text))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitTimedOnceGT(self, ctx:PastTLParser.TimedOnceGTContext):
        child = self.visit(ctx.child)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, Constant('true'), child.output, int(ctx.l.text), None)
        state.output = TimedSetSinceOutput(state, int(ctx.l.text), None)

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    def visitTimedOnce(self, ctx:PastTLParser.TimedOnceContext):
        child = self.visit(ctx.child)

        state = TimedSetState(
            update=None,
            variable=self.meta['tnum']
            )
        state.update = TimedSetSinceUpdate(state, Constant('true'), child.output, int(ctx.l.text), int(ctx.u.text))
        state.output = TimedSetSinceOutput(state, int(ctx.l.text), int(ctx.u.text))

        self.meta['tnum'] += 1
        self.states.append(state)

        return state

    # Visit a parse tree produced by FirstOrderPastMTLParser#Grouping.
    def visitGrouping(self, ctx:PastTLParser.GroupingContext):
        return self.visit(ctx.child)
