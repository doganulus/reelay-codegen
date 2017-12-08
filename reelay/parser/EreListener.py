# Generated from Ere.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EreParser import EreParser
else:
    from EreParser import EreParser

# This class defines a complete listener for a parse tree produced by EreParser.
class EreListener(ParseTreeListener):

    # Enter a parse tree produced by EreParser#Concat.
    def enterConcat(self, ctx:EreParser.ConcatContext):
        pass

    # Exit a parse tree produced by EreParser#Concat.
    def exitConcat(self, ctx:EreParser.ConcatContext):
        pass


    # Enter a parse tree produced by EreParser#Intersect.
    def enterIntersect(self, ctx:EreParser.IntersectContext):
        pass

    # Exit a parse tree produced by EreParser#Intersect.
    def exitIntersect(self, ctx:EreParser.IntersectContext):
        pass


    # Enter a parse tree produced by EreParser#Star.
    def enterStar(self, ctx:EreParser.StarContext):
        pass

    # Exit a parse tree produced by EreParser#Star.
    def exitStar(self, ctx:EreParser.StarContext):
        pass


    # Enter a parse tree produced by EreParser#Restrict.
    def enterRestrict(self, ctx:EreParser.RestrictContext):
        pass

    # Exit a parse tree produced by EreParser#Restrict.
    def exitRestrict(self, ctx:EreParser.RestrictContext):
        pass


    # Enter a parse tree produced by EreParser#Atomic.
    def enterAtomic(self, ctx:EreParser.AtomicContext):
        pass

    # Exit a parse tree produced by EreParser#Atomic.
    def exitAtomic(self, ctx:EreParser.AtomicContext):
        pass


    # Enter a parse tree produced by EreParser#Complement.
    def enterComplement(self, ctx:EreParser.ComplementContext):
        pass

    # Exit a parse tree produced by EreParser#Complement.
    def exitComplement(self, ctx:EreParser.ComplementContext):
        pass


    # Enter a parse tree produced by EreParser#Grouping.
    def enterGrouping(self, ctx:EreParser.GroupingContext):
        pass

    # Exit a parse tree produced by EreParser#Grouping.
    def exitGrouping(self, ctx:EreParser.GroupingContext):
        pass


    # Enter a parse tree produced by EreParser#Question.
    def enterQuestion(self, ctx:EreParser.QuestionContext):
        pass

    # Exit a parse tree produced by EreParser#Question.
    def exitQuestion(self, ctx:EreParser.QuestionContext):
        pass


    # Enter a parse tree produced by EreParser#Plus.
    def enterPlus(self, ctx:EreParser.PlusContext):
        pass

    # Exit a parse tree produced by EreParser#Plus.
    def exitPlus(self, ctx:EreParser.PlusContext):
        pass


    # Enter a parse tree produced by EreParser#Union.
    def enterUnion(self, ctx:EreParser.UnionContext):
        pass

    # Exit a parse tree produced by EreParser#Union.
    def exitUnion(self, ctx:EreParser.UnionContext):
        pass


    # Enter a parse tree produced by EreParser#atom.
    def enterAtom(self, ctx:EreParser.AtomContext):
        pass

    # Exit a parse tree produced by EreParser#atom.
    def exitAtom(self, ctx:EreParser.AtomContext):
        pass


