# Generated from PastLTL.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\35\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3(\n")
        buf.write("\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\63\n\4\3")
        buf.write("\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\5\2\3\4\6\2\4\6\b")
        buf.write("\2\5\3\2\4\5\3\2\6\7\3\2\b\t\2B\2\f\3\2\2\2\4\34\3\2\2")
        buf.write("\2\6\62\3\2\2\2\b\64\3\2\2\2\n\13\7\20\2\2\13\r\7\3\2")
        buf.write("\2\f\n\3\2\2\2\f\r\3\2\2\2\r\16\3\2\2\2\16\17\5\4\3\2")
        buf.write("\17\3\3\2\2\2\20\21\b\3\1\2\21\35\5\6\4\2\22\23\t\2\2")
        buf.write("\2\23\35\5\4\3\t\24\25\7\n\2\2\25\35\5\4\3\6\26\27\7\13")
        buf.write("\2\2\27\35\5\4\3\5\30\31\7\r\2\2\31\32\5\4\3\2\32\33\7")
        buf.write("\16\2\2\33\35\3\2\2\2\34\20\3\2\2\2\34\22\3\2\2\2\34\24")
        buf.write("\3\2\2\2\34\26\3\2\2\2\34\30\3\2\2\2\35)\3\2\2\2\36\37")
        buf.write("\f\b\2\2\37 \t\3\2\2 (\5\4\3\t!\"\f\7\2\2\"#\t\4\2\2#")
        buf.write("(\5\4\3\b$%\f\4\2\2%&\7\f\2\2&(\5\4\3\5\'\36\3\2\2\2\'")
        buf.write("!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\5")
        buf.write("\3\2\2\2+)\3\2\2\2,\63\7\20\2\2-.\7\20\2\2./\7\r\2\2/")
        buf.write("\60\5\b\5\2\60\61\7\16\2\2\61\63\3\2\2\2\62,\3\2\2\2\62")
        buf.write("-\3\2\2\2\63\7\3\2\2\2\649\7\20\2\2\65\66\7\17\2\2\66")
        buf.write("8\7\20\2\2\67\65\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2")
        buf.write("\2:\t\3\2\2\2;9\3\2\2\2\b\f\34\')\629")
        return buf.getvalue()


class PastLTLParser ( Parser ):

    grammarFileName = "PastLTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'!'", "'not'", "'&&'", "'and'", 
                     "'||'", "'or'", "'once'", "'always'", "'since'", "'('", 
                     "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "WS" ]

    RULE_namedExpr = 0
    RULE_expr = 1
    RULE_atom = 2
    RULE_idlist = 3

    ruleNames =  [ "namedExpr", "expr", "atom", "idlist" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    IDENTIFIER=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NamedExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.child = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(PastLTLParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(PastLTLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PastLTLParser.RULE_namedExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedExpr" ):
                listener.enterNamedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedExpr" ):
                listener.exitNamedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedExpr" ):
                return visitor.visitNamedExpr(self)
            else:
                return visitor.visitChildren(self)




    def namedExpr(self):

        localctx = PastLTLParser.NamedExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_namedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                localctx.name = self.match(PastLTLParser.IDENTIFIER)
                self.state = 9
                self.match(PastLTLParser.T__0)


            self.state = 12
            localctx.child = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PastLTLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DisjunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PastLTLParser.ExprContext)
            else:
                return self.getTypedRuleContext(PastLTLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class OnceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOnce" ):
                listener.enterOnce(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOnce" ):
                listener.exitOnce(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnce" ):
                return visitor.visitOnce(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PastLTLParser.ExprContext)
            else:
                return self.getTypedRuleContext(PastLTLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class SinceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PastLTLParser.ExprContext)
            else:
                return self.getTypedRuleContext(PastLTLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSince" ):
                listener.enterSince(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSince" ):
                listener.exitSince(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSince" ):
                return visitor.visitSince(self)
            else:
                return visitor.visitChildren(self)


    class AtomicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PastLTLParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic" ):
                listener.enterAtomic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic" ):
                listener.exitAtomic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic" ):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)


    class GroupingContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping" ):
                listener.enterGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping" ):
                listener.exitGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping" ):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PastLTLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlways" ):
                listener.enterAlways(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlways" ):
                listener.exitAlways(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlways" ):
                return visitor.visitAlways(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PastLTLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PastLTLParser.IDENTIFIER]:
                localctx = PastLTLParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                localctx.child = self.atom()
                pass
            elif token in [PastLTLParser.T__1, PastLTLParser.T__2]:
                localctx = PastLTLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                _la = self._input.LA(1)
                if not(_la==PastLTLParser.T__1 or _la==PastLTLParser.T__2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                localctx.child = self.expr(7)
                pass
            elif token in [PastLTLParser.T__7]:
                localctx = PastLTLParser.OnceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(PastLTLParser.T__7)
                self.state = 19
                localctx.child = self.expr(4)
                pass
            elif token in [PastLTLParser.T__8]:
                localctx = PastLTLParser.AlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(PastLTLParser.T__8)
                self.state = 21
                localctx.child = self.expr(3)
                pass
            elif token in [PastLTLParser.T__10]:
                localctx = PastLTLParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(PastLTLParser.T__10)
                self.state = 23
                localctx.child = self.expr(0)
                self.state = 24
                self.match(PastLTLParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PastLTLParser.ConjunctionContext(self, PastLTLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==PastLTLParser.T__3 or _la==PastLTLParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = PastLTLParser.DisjunctionContext(self, PastLTLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not(_la==PastLTLParser.T__5 or _la==PastLTLParser.T__6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = PastLTLParser.SinceContext(self, PastLTLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(PastLTLParser.T__9)
                        self.state = 36
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PastLTLParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PastLTLParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProp" ):
                listener.enterProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProp" ):
                listener.exitProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProp" ):
                return visitor.visitProp(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PastLTLParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.args = None # IdlistContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PastLTLParser.IDENTIFIER, 0)
        def idlist(self):
            return self.getTypedRuleContext(PastLTLParser.IdlistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = PastLTLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = PastLTLParser.PropContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                localctx.name = self.match(PastLTLParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = PastLTLParser.PredContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                localctx.name = self.match(PastLTLParser.IDENTIFIER)
                self.state = 44
                self.match(PastLTLParser.T__10)
                self.state = 45
                localctx.args = self.idlist()
                self.state = 46
                self.match(PastLTLParser.T__11)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.param = None # Token

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PastLTLParser.IDENTIFIER)
            else:
                return self.getToken(PastLTLParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return PastLTLParser.RULE_idlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlist" ):
                listener.enterIdlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlist" ):
                listener.exitIdlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = PastLTLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            localctx.param = self.match(PastLTLParser.IDENTIFIER)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PastLTLParser.T__12:
                self.state = 51
                self.match(PastLTLParser.T__12)
                self.state = 52
                localctx.param = self.match(PastLTLParser.IDENTIFIER)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




