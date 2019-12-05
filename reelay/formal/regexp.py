from antlr4 import *

from reelay.parser.RegExpLexer import RegExpLexer
from reelay.parser.RegExpParser import RegExpParser
from reelay.parser.RegExpVisitor import RegExpVisitor

from reelay.machine.common import *
from reelay.machine.boolean import *
from reelay.machine.timed import *

class RegExpTreeAnnotator(RegExpVisitor):

    def __init__(self):
        super().__init__()

    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.prev_output = ctx.child.prev_output

    def visitAtomic(self, ctx:RegExpParser.AtomicContext):
        
        # self.visit(ctx.child)

        ctx.state = BooleanState(
            # update=BooleanAnd(Atom(name, dtype), ctx.trigger),
            update=None,
            variable=None
            )

        ctx.nullable = False
        ctx.output = ctx.state.output
        ctx.prev_output = Pre(ctx.state.output)

    # def visitVarConst(self, ctx:RegExpParser.VarConstContext):

    #     self.visit(ctx.child)

    #     ctx.nullable = ctx.child.nullable
    #     ctx.output = ctx.child.output

    def visitUnion(self, ctx:RegExpParser.UnionContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable or ctx.right.nullable
        ctx.output = BooleanOr(ctx.left.output, ctx.right.output)
        ctx.prev_output = BooleanOr(ctx.left.prev_output, ctx.right.prev_output)

    # Visit a parse tree produced by RegExpParser#Concat.
    def visitConcatenation(self, ctx:RegExpParser.ConcatenationContext):

        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable and ctx.right.nullable
        ctx.output = BooleanOr(ctx.left.output, ctx.right.output) if ctx.right.nullable else ctx.right.output
        ctx.prev_output = BooleanOr(ctx.left.prev_output, ctx.right.prev_output) if ctx.right.nullable else ctx.right.prev_output

    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output
        ctx.prev_output = ctx.child.prev_output

    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable 
        ctx.output = ctx.child.output
        ctx.prev_output = ctx.child.prev_output

    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output
        ctx.prev_output = ctx.child.prev_output

    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitComplementation(self, ctx:RegExpParser.ComplementationContext):

        self.visit(ctx.child)

        ctx.nullable = False
        ctx.output = BooleanNot(ctx.child.output)
        ctx.prev_output = BooleanNot(ctx.child.prev_output)

    def visitIntersection(self, ctx:RegExpParser.IntersectionContext):

        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable and ctx.right.nullable
        ctx.output = BooleanAnd(ctx.left.output, ctx.right.output)
        ctx.prev_output = BooleanAnd(ctx.left.prev_output, ctx.right.prev_output)


    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.prev_output = ctx.child.prev_output

class RegExpBuilder(RegExpVisitor):

    def __init__(self):
        super().__init__()
        self.states = list()
        self.meta = dict(name='name', bnum=0, tnum=0, vars=set(), funcs=set())

    def build(self, expr):

        lexer = RegExpLexer(InputStream(expr))
        stream = CommonTokenStream(lexer)
        parser = RegExpParser(stream)
        tree = parser.namedExpr()

        annotator = RegExpTreeAnnotator()
        annotator.visit(tree)

        self.meta['expr'] = expr

        child = self.visit_with(tree, Constant('true'))

        return self.states, self.meta

    def visit_with(self, tree, trigger):
        tree.trigger = trigger
        return self.visit(tree)

    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):

        self.visit_with(ctx.child, ctx.trigger)

        try:
            name = ctx.name.text
        except AttributeError as e:
            name = 'Expr'

        self.meta['name'] = name
        self.meta['output'] = BooleanOr(ctx.output, ctx.nullable)

    def visitAtomList(self, ctx:RegExpParser.AtomListContext):
        uncomma = [child for child in ctx.children if child.getText() != ',']
        return [self.visit(child) for child in uncomma]

    def visitConstant(self, ctx:RegExpParser.ConstantContext):
        return Constant(ctx.getText())

    def visitAtomic(self, ctx:RegExpParser.AtomicContext):

        atom = self.visit(ctx.child)
        
        ctx.state.update = BooleanAnd(atom, ctx.trigger)
        ctx.state.variable = self.meta['bnum']

        self.meta['bnum'] += 1
        self.states.append(ctx.state)
      

    def visitProp(self, ctx:RegExpParser.PropContext):

        try:
            name, dtype = ctx.name.text.split(':')
        except:
            name = ctx.name.text
            dtype = 'bool'

        self.meta['vars'] = self.meta['vars'] | set([(dtype, name)])

        return Atom(name, dtype)

    def visitPred(self, ctx:RegExpParser.PredContext):

        args = self.visit(ctx.args)

        try:
            name, dtype = ctx.name.text.split(':')
        except:
            name = ctx.name.text
            dtype = 'bool'
        # args = ','.join([str(atom) for atom in atoms])

        self.meta['funcs'] = self.meta['funcs'] | set([(dtype, name)])

        return Atom(name, dtype, args)

    def visitVarConst(self, ctx:RegExpParser.VarConstContext):
        return self.visit(ctx.child)

    def visitVarBind(self, ctx:RegExpParser.VarBindContext):
        raise NotImplementedError

    def visitComplementation(self, ctx:RegExpParser.ComplementationContext):
        raise NotImplementedError

    def visitUnion(self, ctx:RegExpParser.UnionContext):

        self.visit_with(ctx.left, ctx.trigger)
        self.visit_with(ctx.right, ctx.trigger)

    def visitConcatenation(self, ctx:RegExpParser.ConcatenationContext):

        self.visit_with(ctx.left, ctx.trigger)

        if ctx.left.nullable:
            self.visit_with(ctx.right, BooleanOr(ctx.left.prev_output, ctx.trigger))
        else:
            self.visit_with(ctx.right, ctx.left.prev_output)

    def visitStar(self, ctx:RegExpParser.StarContext):
        self.visit_with(ctx.child, BooleanOr(ctx.child.prev_output, ctx.trigger))

    def visitPlus(self, ctx:RegExpParser.PlusContext):
        self.visit_with(ctx.child, BooleanOr(ctx.child.prev_output, ctx.trigger))

    def visitQuestion(self, ctx:RegExpParser.QuestionContext):
        self.visit_with(ctx.child, ctx.trigger)

    def visitIntersection(self, ctx:RegExpParser.IntersectionContext):
        self.visit_with(ctx.left, ctx.trigger)
        self.visit_with(ctx.right, ctx.trigger)

    def visitGrouping(self, ctx:RegExpParser.GroupingContext):
        self.visit_with(ctx.child, ctx.trigger)
