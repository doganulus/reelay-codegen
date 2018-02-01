# Generated from PastLTL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PastLTLParser import PastLTLParser
else:
    from PastLTLParser import PastLTLParser

# This class defines a complete generic visitor for a parse tree produced by PastLTLParser.

class PastLTLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PastLTLParser#namedExpr.
    def visitNamedExpr(self, ctx:PastLTLParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Disjunction.
    def visitDisjunction(self, ctx:PastLTLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Negation.
    def visitNegation(self, ctx:PastLTLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Once.
    def visitOnce(self, ctx:PastLTLParser.OnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Conjunction.
    def visitConjunction(self, ctx:PastLTLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Since.
    def visitSince(self, ctx:PastLTLParser.SinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Atomic.
    def visitAtomic(self, ctx:PastLTLParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Grouping.
    def visitGrouping(self, ctx:PastLTLParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Always.
    def visitAlways(self, ctx:PastLTLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Prop.
    def visitProp(self, ctx:PastLTLParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#Pred.
    def visitPred(self, ctx:PastLTLParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastLTLParser#idlist.
    def visitIdlist(self, ctx:PastLTLParser.IdlistContext):
        return self.visitChildren(ctx)



del PastLTLParser