# Generated from PastTL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PastTLParser import PastTLParser
else:
    from PastTLParser import PastTLParser

# This class defines a complete listener for a parse tree produced by PastTLParser.
class PastTLListener(ParseTreeListener):

    # Enter a parse tree produced by PastTLParser#namedExpr.
    def enterNamedExpr(self, ctx:PastTLParser.NamedExprContext):
        pass

    # Exit a parse tree produced by PastTLParser#namedExpr.
    def exitNamedExpr(self, ctx:PastTLParser.NamedExprContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedAlways.
    def enterTimedAlways(self, ctx:PastTLParser.TimedAlwaysContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedAlways.
    def exitTimedAlways(self, ctx:PastTLParser.TimedAlwaysContext):
        pass


    # Enter a parse tree produced by PastTLParser#Negation.
    def enterNegation(self, ctx:PastTLParser.NegationContext):
        pass

    # Exit a parse tree produced by PastTLParser#Negation.
    def exitNegation(self, ctx:PastTLParser.NegationContext):
        pass


    # Enter a parse tree produced by PastTLParser#Once.
    def enterOnce(self, ctx:PastTLParser.OnceContext):
        pass

    # Exit a parse tree produced by PastTLParser#Once.
    def exitOnce(self, ctx:PastTLParser.OnceContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedSince.
    def enterTimedSince(self, ctx:PastTLParser.TimedSinceContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedSince.
    def exitTimedSince(self, ctx:PastTLParser.TimedSinceContext):
        pass


    # Enter a parse tree produced by PastTLParser#Atomic.
    def enterAtomic(self, ctx:PastTLParser.AtomicContext):
        pass

    # Exit a parse tree produced by PastTLParser#Atomic.
    def exitAtomic(self, ctx:PastTLParser.AtomicContext):
        pass


    # Enter a parse tree produced by PastTLParser#Grouping.
    def enterGrouping(self, ctx:PastTLParser.GroupingContext):
        pass

    # Exit a parse tree produced by PastTLParser#Grouping.
    def exitGrouping(self, ctx:PastTLParser.GroupingContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedSinceLT.
    def enterTimedSinceLT(self, ctx:PastTLParser.TimedSinceLTContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedSinceLT.
    def exitTimedSinceLT(self, ctx:PastTLParser.TimedSinceLTContext):
        pass


    # Enter a parse tree produced by PastTLParser#Implication.
    def enterImplication(self, ctx:PastTLParser.ImplicationContext):
        pass

    # Exit a parse tree produced by PastTLParser#Implication.
    def exitImplication(self, ctx:PastTLParser.ImplicationContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedAlwaysGT.
    def enterTimedAlwaysGT(self, ctx:PastTLParser.TimedAlwaysGTContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedAlwaysGT.
    def exitTimedAlwaysGT(self, ctx:PastTLParser.TimedAlwaysGTContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedOnce.
    def enterTimedOnce(self, ctx:PastTLParser.TimedOnceContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedOnce.
    def exitTimedOnce(self, ctx:PastTLParser.TimedOnceContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedSinceGT.
    def enterTimedSinceGT(self, ctx:PastTLParser.TimedSinceGTContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedSinceGT.
    def exitTimedSinceGT(self, ctx:PastTLParser.TimedSinceGTContext):
        pass


    # Enter a parse tree produced by PastTLParser#Disjunction.
    def enterDisjunction(self, ctx:PastTLParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by PastTLParser#Disjunction.
    def exitDisjunction(self, ctx:PastTLParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedAlwaysLT.
    def enterTimedAlwaysLT(self, ctx:PastTLParser.TimedAlwaysLTContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedAlwaysLT.
    def exitTimedAlwaysLT(self, ctx:PastTLParser.TimedAlwaysLTContext):
        pass


    # Enter a parse tree produced by PastTLParser#Exists.
    def enterExists(self, ctx:PastTLParser.ExistsContext):
        pass

    # Exit a parse tree produced by PastTLParser#Exists.
    def exitExists(self, ctx:PastTLParser.ExistsContext):
        pass


    # Enter a parse tree produced by PastTLParser#Conjunction.
    def enterConjunction(self, ctx:PastTLParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by PastTLParser#Conjunction.
    def exitConjunction(self, ctx:PastTLParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by PastTLParser#Previous.
    def enterPrevious(self, ctx:PastTLParser.PreviousContext):
        pass

    # Exit a parse tree produced by PastTLParser#Previous.
    def exitPrevious(self, ctx:PastTLParser.PreviousContext):
        pass


    # Enter a parse tree produced by PastTLParser#Since.
    def enterSince(self, ctx:PastTLParser.SinceContext):
        pass

    # Exit a parse tree produced by PastTLParser#Since.
    def exitSince(self, ctx:PastTLParser.SinceContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedOnceGT.
    def enterTimedOnceGT(self, ctx:PastTLParser.TimedOnceGTContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedOnceGT.
    def exitTimedOnceGT(self, ctx:PastTLParser.TimedOnceGTContext):
        pass


    # Enter a parse tree produced by PastTLParser#Always.
    def enterAlways(self, ctx:PastTLParser.AlwaysContext):
        pass

    # Exit a parse tree produced by PastTLParser#Always.
    def exitAlways(self, ctx:PastTLParser.AlwaysContext):
        pass


    # Enter a parse tree produced by PastTLParser#TimedOnceLT.
    def enterTimedOnceLT(self, ctx:PastTLParser.TimedOnceLTContext):
        pass

    # Exit a parse tree produced by PastTLParser#TimedOnceLT.
    def exitTimedOnceLT(self, ctx:PastTLParser.TimedOnceLTContext):
        pass


    # Enter a parse tree produced by PastTLParser#VarConst.
    def enterVarConst(self, ctx:PastTLParser.VarConstContext):
        pass

    # Exit a parse tree produced by PastTLParser#VarConst.
    def exitVarConst(self, ctx:PastTLParser.VarConstContext):
        pass


    # Enter a parse tree produced by PastTLParser#VarBind.
    def enterVarBind(self, ctx:PastTLParser.VarBindContext):
        pass

    # Exit a parse tree produced by PastTLParser#VarBind.
    def exitVarBind(self, ctx:PastTLParser.VarBindContext):
        pass


    # Enter a parse tree produced by PastTLParser#Prop.
    def enterProp(self, ctx:PastTLParser.PropContext):
        pass

    # Exit a parse tree produced by PastTLParser#Prop.
    def exitProp(self, ctx:PastTLParser.PropContext):
        pass


    # Enter a parse tree produced by PastTLParser#Pred.
    def enterPred(self, ctx:PastTLParser.PredContext):
        pass

    # Exit a parse tree produced by PastTLParser#Pred.
    def exitPred(self, ctx:PastTLParser.PredContext):
        pass


    # Enter a parse tree produced by PastTLParser#Constant.
    def enterConstant(self, ctx:PastTLParser.ConstantContext):
        pass

    # Exit a parse tree produced by PastTLParser#Constant.
    def exitConstant(self, ctx:PastTLParser.ConstantContext):
        pass


    # Enter a parse tree produced by PastTLParser#AtomList.
    def enterAtomList(self, ctx:PastTLParser.AtomListContext):
        pass

    # Exit a parse tree produced by PastTLParser#AtomList.
    def exitAtomList(self, ctx:PastTLParser.AtomListContext):
        pass


    # Enter a parse tree produced by PastTLParser#idlist.
    def enterIdlist(self, ctx:PastTLParser.IdlistContext):
        pass

    # Exit a parse tree produced by PastTLParser#idlist.
    def exitIdlist(self, ctx:PastTLParser.IdlistContext):
        pass


