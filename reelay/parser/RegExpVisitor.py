# Generated from RegExp.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegExpParser import RegExpParser
else:
    from RegExpParser import RegExpParser

# This class defines a complete generic visitor for a parse tree produced by RegExpParser.

class RegExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegExpParser#namedExpr.
    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Intersection.
    def visitIntersection(self, ctx:RegExpParser.IntersectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Atomic.
    def visitAtomic(self, ctx:RegExpParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Union.
    def visitUnion(self, ctx:RegExpParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Concatenation.
    def visitConcatenation(self, ctx:RegExpParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Exists.
    def visitExists(self, ctx:RegExpParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#RestrictGT.
    def visitRestrictGT(self, ctx:RegExpParser.RestrictGTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Restrict.
    def visitRestrict(self, ctx:RegExpParser.RestrictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Complementation.
    def visitComplementation(self, ctx:RegExpParser.ComplementationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#RestrictLT.
    def visitRestrictLT(self, ctx:RegExpParser.RestrictLTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#VarConst.
    def visitVarConst(self, ctx:RegExpParser.VarConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#VarBind.
    def visitVarBind(self, ctx:RegExpParser.VarBindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Prop.
    def visitProp(self, ctx:RegExpParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Pred.
    def visitPred(self, ctx:RegExpParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Constant.
    def visitConstant(self, ctx:RegExpParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#AtomList.
    def visitAtomList(self, ctx:RegExpParser.AtomListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#idlist.
    def visitIdlist(self, ctx:RegExpParser.IdlistContext):
        return self.visitChildren(ctx)



del RegExpParser