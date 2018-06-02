# Generated from PastTL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PastTLParser import PastTLParser
else:
    from PastTLParser import PastTLParser

# This class defines a complete generic visitor for a parse tree produced by PastTLParser.

class PastTLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PastTLParser#namedExpr.
    def visitNamedExpr(self, ctx:PastTLParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedAlways.
    def visitTimedAlways(self, ctx:PastTLParser.TimedAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Negation.
    def visitNegation(self, ctx:PastTLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Once.
    def visitOnce(self, ctx:PastTLParser.OnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedSince.
    def visitTimedSince(self, ctx:PastTLParser.TimedSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Atomic.
    def visitAtomic(self, ctx:PastTLParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Grouping.
    def visitGrouping(self, ctx:PastTLParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedSinceLT.
    def visitTimedSinceLT(self, ctx:PastTLParser.TimedSinceLTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Implication.
    def visitImplication(self, ctx:PastTLParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedAlwaysGT.
    def visitTimedAlwaysGT(self, ctx:PastTLParser.TimedAlwaysGTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedOnce.
    def visitTimedOnce(self, ctx:PastTLParser.TimedOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedSinceGT.
    def visitTimedSinceGT(self, ctx:PastTLParser.TimedSinceGTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Disjunction.
    def visitDisjunction(self, ctx:PastTLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedAlwaysLT.
    def visitTimedAlwaysLT(self, ctx:PastTLParser.TimedAlwaysLTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Exists.
    def visitExists(self, ctx:PastTLParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Conjunction.
    def visitConjunction(self, ctx:PastTLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Previous.
    def visitPrevious(self, ctx:PastTLParser.PreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Since.
    def visitSince(self, ctx:PastTLParser.SinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedOnceGT.
    def visitTimedOnceGT(self, ctx:PastTLParser.TimedOnceGTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Always.
    def visitAlways(self, ctx:PastTLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#TimedOnceLT.
    def visitTimedOnceLT(self, ctx:PastTLParser.TimedOnceLTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#VarConst.
    def visitVarConst(self, ctx:PastTLParser.VarConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#VarBind.
    def visitVarBind(self, ctx:PastTLParser.VarBindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Prop.
    def visitProp(self, ctx:PastTLParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Pred.
    def visitPred(self, ctx:PastTLParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#Constant.
    def visitConstant(self, ctx:PastTLParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#AtomList.
    def visitAtomList(self, ctx:PastTLParser.AtomListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastTLParser#idlist.
    def visitIdlist(self, ctx:PastTLParser.IdlistContext):
        return self.visitChildren(ctx)



del PastTLParser