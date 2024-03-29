# Generated from RegExp.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegExpParser import RegExpParser
else:
    from RegExpParser import RegExpParser

# This class defines a complete listener for a parse tree produced by RegExpParser.
class RegExpListener(ParseTreeListener):

    # Enter a parse tree produced by RegExpParser#namedExpr.
    def enterNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        pass

    # Exit a parse tree produced by RegExpParser#namedExpr.
    def exitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        pass


    # Enter a parse tree produced by RegExpParser#Intersection.
    def enterIntersection(self, ctx:RegExpParser.IntersectionContext):
        pass

    # Exit a parse tree produced by RegExpParser#Intersection.
    def exitIntersection(self, ctx:RegExpParser.IntersectionContext):
        pass


    # Enter a parse tree produced by RegExpParser#Atomic.
    def enterAtomic(self, ctx:RegExpParser.AtomicContext):
        pass

    # Exit a parse tree produced by RegExpParser#Atomic.
    def exitAtomic(self, ctx:RegExpParser.AtomicContext):
        pass


    # Enter a parse tree produced by RegExpParser#Grouping.
    def enterGrouping(self, ctx:RegExpParser.GroupingContext):
        pass

    # Exit a parse tree produced by RegExpParser#Grouping.
    def exitGrouping(self, ctx:RegExpParser.GroupingContext):
        pass


    # Enter a parse tree produced by RegExpParser#Union.
    def enterUnion(self, ctx:RegExpParser.UnionContext):
        pass

    # Exit a parse tree produced by RegExpParser#Union.
    def exitUnion(self, ctx:RegExpParser.UnionContext):
        pass


    # Enter a parse tree produced by RegExpParser#Concatenation.
    def enterConcatenation(self, ctx:RegExpParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by RegExpParser#Concatenation.
    def exitConcatenation(self, ctx:RegExpParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by RegExpParser#Star.
    def enterStar(self, ctx:RegExpParser.StarContext):
        pass

    # Exit a parse tree produced by RegExpParser#Star.
    def exitStar(self, ctx:RegExpParser.StarContext):
        pass


    # Enter a parse tree produced by RegExpParser#Exists.
    def enterExists(self, ctx:RegExpParser.ExistsContext):
        pass

    # Exit a parse tree produced by RegExpParser#Exists.
    def exitExists(self, ctx:RegExpParser.ExistsContext):
        pass


    # Enter a parse tree produced by RegExpParser#RestrictGT.
    def enterRestrictGT(self, ctx:RegExpParser.RestrictGTContext):
        pass

    # Exit a parse tree produced by RegExpParser#RestrictGT.
    def exitRestrictGT(self, ctx:RegExpParser.RestrictGTContext):
        pass


    # Enter a parse tree produced by RegExpParser#Restrict.
    def enterRestrict(self, ctx:RegExpParser.RestrictContext):
        pass

    # Exit a parse tree produced by RegExpParser#Restrict.
    def exitRestrict(self, ctx:RegExpParser.RestrictContext):
        pass


    # Enter a parse tree produced by RegExpParser#Complementation.
    def enterComplementation(self, ctx:RegExpParser.ComplementationContext):
        pass

    # Exit a parse tree produced by RegExpParser#Complementation.
    def exitComplementation(self, ctx:RegExpParser.ComplementationContext):
        pass


    # Enter a parse tree produced by RegExpParser#Question.
    def enterQuestion(self, ctx:RegExpParser.QuestionContext):
        pass

    # Exit a parse tree produced by RegExpParser#Question.
    def exitQuestion(self, ctx:RegExpParser.QuestionContext):
        pass


    # Enter a parse tree produced by RegExpParser#RestrictLT.
    def enterRestrictLT(self, ctx:RegExpParser.RestrictLTContext):
        pass

    # Exit a parse tree produced by RegExpParser#RestrictLT.
    def exitRestrictLT(self, ctx:RegExpParser.RestrictLTContext):
        pass


    # Enter a parse tree produced by RegExpParser#Plus.
    def enterPlus(self, ctx:RegExpParser.PlusContext):
        pass

    # Exit a parse tree produced by RegExpParser#Plus.
    def exitPlus(self, ctx:RegExpParser.PlusContext):
        pass


    # Enter a parse tree produced by RegExpParser#VarConst.
    def enterVarConst(self, ctx:RegExpParser.VarConstContext):
        pass

    # Exit a parse tree produced by RegExpParser#VarConst.
    def exitVarConst(self, ctx:RegExpParser.VarConstContext):
        pass


    # Enter a parse tree produced by RegExpParser#VarBind.
    def enterVarBind(self, ctx:RegExpParser.VarBindContext):
        pass

    # Exit a parse tree produced by RegExpParser#VarBind.
    def exitVarBind(self, ctx:RegExpParser.VarBindContext):
        pass


    # Enter a parse tree produced by RegExpParser#Prop.
    def enterProp(self, ctx:RegExpParser.PropContext):
        pass

    # Exit a parse tree produced by RegExpParser#Prop.
    def exitProp(self, ctx:RegExpParser.PropContext):
        pass


    # Enter a parse tree produced by RegExpParser#Pred.
    def enterPred(self, ctx:RegExpParser.PredContext):
        pass

    # Exit a parse tree produced by RegExpParser#Pred.
    def exitPred(self, ctx:RegExpParser.PredContext):
        pass


    # Enter a parse tree produced by RegExpParser#Constant.
    def enterConstant(self, ctx:RegExpParser.ConstantContext):
        pass

    # Exit a parse tree produced by RegExpParser#Constant.
    def exitConstant(self, ctx:RegExpParser.ConstantContext):
        pass


    # Enter a parse tree produced by RegExpParser#AtomList.
    def enterAtomList(self, ctx:RegExpParser.AtomListContext):
        pass

    # Exit a parse tree produced by RegExpParser#AtomList.
    def exitAtomList(self, ctx:RegExpParser.AtomListContext):
        pass


    # Enter a parse tree produced by RegExpParser#idlist.
    def enterIdlist(self, ctx:RegExpParser.IdlistContext):
        pass

    # Exit a parse tree produced by RegExpParser#idlist.
    def exitIdlist(self, ctx:RegExpParser.IdlistContext):
        pass


