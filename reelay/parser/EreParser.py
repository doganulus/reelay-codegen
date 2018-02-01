# Generated from Ere.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\7\2-\n\2\f\2\16\2\60\13\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\2\3\2\5\2\4\6\2\2\2")
        buf.write("C\2\25\3\2\2\2\4\61\3\2\2\2\6\63\3\2\2\2\b\t\b\2\1\2\t")
        buf.write("\26\5\4\3\2\n\13\7\3\2\2\13\f\5\6\4\2\f\r\7\4\2\2\r\16")
        buf.write("\5\2\2\f\16\26\3\2\2\2\17\20\7\5\2\2\20\26\5\2\2\13\21")
        buf.write("\22\7\17\2\2\22\23\5\2\2\2\23\24\7\20\2\2\24\26\3\2\2")
        buf.write("\2\25\b\3\2\2\2\25\n\3\2\2\2\25\17\3\2\2\2\25\21\3\2\2")
        buf.write("\2\26.\3\2\2\2\27\30\f\t\2\2\30\31\7\t\2\2\31-\5\2\2\n")
        buf.write("\32\33\f\5\2\2\33\34\7\r\2\2\34-\5\2\2\6\35\36\f\4\2\2")
        buf.write("\36\37\7\16\2\2\37-\5\2\2\5 !\f\n\2\2!\"\7\6\2\2\"#\7")
        buf.write("\22\2\2#$\7\7\2\2$%\7\22\2\2%-\7\b\2\2&\'\f\b\2\2\'-\7")
        buf.write("\n\2\2()\f\7\2\2)-\7\13\2\2*+\f\6\2\2+-\7\f\2\2,\27\3")
        buf.write("\2\2\2,\32\3\2\2\2,\35\3\2\2\2, \3\2\2\2,&\3\2\2\2,(\3")
        buf.write("\2\2\2,*\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\3\3")
        buf.write("\2\2\2\60.\3\2\2\2\61\62\7\21\2\2\62\5\3\2\2\2\638\7\21")
        buf.write("\2\2\64\65\7\7\2\2\65\67\7\21\2\2\66\64\3\2\2\2\67:\3")
        buf.write("\2\2\28\66\3\2\2\289\3\2\2\29\7\3\2\2\2:8\3\2\2\2\6\25")
        buf.write(",.8")
        return buf.getvalue()


class EreParser ( Parser ):

    grammarFileName = "Ere.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'exists'", "'.'", "'~'", "'{'", "','", 
                     "'}'", "'&'", "'*'", "'+'", "'?'", "';'", "'|'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_atom = 1
    RULE_idlist = 2

    ruleNames =  [ "expr", "atom", "idlist" ]

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
    T__13=14
    IDENTIFIER=15
    NUMBER=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EreParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EreParser.ExprContext)
            else:
                return self.getTypedRuleContext(EreParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)


    class IntersectContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EreParser.ExprContext)
            else:
                return self.getTypedRuleContext(EreParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntersect" ):
                listener.enterIntersect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntersect" ):
                listener.exitIntersect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntersect" ):
                return visitor.visitIntersect(self)
            else:
                return visitor.visitChildren(self)


    class StarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar" ):
                listener.enterStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar" ):
                listener.exitStar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar" ):
                return visitor.visitStar(self)
            else:
                return visitor.visitChildren(self)


    class ExistsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.variables = None # IdlistContext
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def idlist(self):
            return self.getTypedRuleContext(EreParser.IdlistContext,0)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExists" ):
                listener.enterExists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExists" ):
                listener.exitExists(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExists" ):
                return visitor.visitExists(self)
            else:
                return visitor.visitChildren(self)


    class RestrictContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.min_val = None # Token
            self.max_val = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(EreParser.NUMBER)
            else:
                return self.getToken(EreParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestrict" ):
                listener.enterRestrict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestrict" ):
                listener.exitRestrict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestrict" ):
                return visitor.visitRestrict(self)
            else:
                return visitor.visitChildren(self)


    class AtomicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(EreParser.AtomContext,0)


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


    class ComplementContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplement" ):
                listener.enterComplement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplement" ):
                listener.exitComplement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplement" ):
                return visitor.visitComplement(self)
            else:
                return visitor.visitChildren(self)


    class GroupingContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)


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


    class QuestionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion" ):
                listener.enterQuestion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion" ):
                listener.exitQuestion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion" ):
                return visitor.visitQuestion(self)
            else:
                return visitor.visitChildren(self)


    class PlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EreParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)


    class UnionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EreParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EreParser.ExprContext)
            else:
                return self.getTypedRuleContext(EreParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion" ):
                return visitor.visitUnion(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EreParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EreParser.IDENTIFIER]:
                localctx = EreParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                localctx.child = self.atom()
                pass
            elif token in [EreParser.T__0]:
                localctx = EreParser.ExistsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(EreParser.T__0)
                self.state = 9
                localctx.variables = self.idlist()
                self.state = 10
                self.match(EreParser.T__1)
                self.state = 11
                localctx.child = self.expr(10)
                pass
            elif token in [EreParser.T__2]:
                localctx = EreParser.ComplementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(EreParser.T__2)
                self.state = 14
                localctx.child = self.expr(9)
                pass
            elif token in [EreParser.T__12]:
                localctx = EreParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(EreParser.T__12)
                self.state = 16
                localctx.child = self.expr(0)
                self.state = 17
                self.match(EreParser.T__13)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = EreParser.IntersectContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 22
                        self.match(EreParser.T__6)
                        self.state = 23
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = EreParser.ConcatContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 25
                        self.match(EreParser.T__10)
                        self.state = 26
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = EreParser.UnionContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 28
                        self.match(EreParser.T__11)
                        self.state = 29
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = EreParser.RestrictContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 31
                        self.match(EreParser.T__3)
                        self.state = 32
                        localctx.min_val = self.match(EreParser.NUMBER)
                        self.state = 33
                        self.match(EreParser.T__4)
                        self.state = 34
                        localctx.max_val = self.match(EreParser.NUMBER)
                        self.state = 35
                        self.match(EreParser.T__5)
                        pass

                    elif la_ == 5:
                        localctx = EreParser.StarContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        self.match(EreParser.T__7)
                        pass

                    elif la_ == 6:
                        localctx = EreParser.PlusContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        self.match(EreParser.T__8)
                        pass

                    elif la_ == 7:
                        localctx = EreParser.QuestionContext(self, EreParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(EreParser.T__9)
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def IDENTIFIER(self):
            return self.getToken(EreParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return EreParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = EreParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(EreParser.IDENTIFIER)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(EreParser.IDENTIFIER)
            else:
                return self.getToken(EreParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return EreParser.RULE_idlist

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

        localctx = EreParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(EreParser.IDENTIFIER)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EreParser.T__4:
                self.state = 50
                self.match(EreParser.T__4)
                self.state = 51
                self.match(EreParser.IDENTIFIER)
                self.state = 56
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
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         




