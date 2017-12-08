# Generated from Ere.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EreParser import EreParser
else:
    from EreParser import EreParser

# This class defines a complete generic visitor for a parse tree produced by EreParser.

class EreVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EreParser#Concat.
    def visitConcat(self, ctx:EreParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Intersect.
    def visitIntersect(self, ctx:EreParser.IntersectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Star.
    def visitStar(self, ctx:EreParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Restrict.
    def visitRestrict(self, ctx:EreParser.RestrictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Atomic.
    def visitAtomic(self, ctx:EreParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Complement.
    def visitComplement(self, ctx:EreParser.ComplementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Grouping.
    def visitGrouping(self, ctx:EreParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Question.
    def visitQuestion(self, ctx:EreParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Plus.
    def visitPlus(self, ctx:EreParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#Union.
    def visitUnion(self, ctx:EreParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EreParser#atom.
    def visitAtom(self, ctx:EreParser.AtomContext):
        return self.visitChildren(ctx)



del EreParser