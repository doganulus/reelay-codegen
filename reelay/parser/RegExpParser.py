# Generated from RegExp.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\5\2\21\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3D\n\3\f\3\16\3G\13\3\3\4\3\4\3\4\3\4\5\4M\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5V\n\5\3\6\3\6\3\6\7\6[\n\6\f")
        buf.write("\6\16\6^\13\6\3\7\3\7\3\7\7\7c\n\7\f\7\16\7f\13\7\3\7")
        buf.write("\2\3\4\b\2\4\6\b\n\f\2\3\3\2\25\26\2s\2\20\3\2\2\2\4\"")
        buf.write("\3\2\2\2\6L\3\2\2\2\bU\3\2\2\2\nW\3\2\2\2\f_\3\2\2\2\16")
        buf.write("\17\7\25\2\2\17\21\7\3\2\2\20\16\3\2\2\2\20\21\3\2\2\2")
        buf.write("\21\22\3\2\2\2\22\23\5\4\3\2\23\3\3\2\2\2\24\25\b\3\1")
        buf.write("\2\25#\5\6\4\2\26\27\7\4\2\2\27\30\7\5\2\2\30\31\5\f\7")
        buf.write("\2\31\32\7\6\2\2\32\33\5\4\3\16\33#\3\2\2\2\34\35\7\7")
        buf.write("\2\2\35#\5\4\3\r\36\37\7\23\2\2\37 \5\4\3\2 !\7\24\2\2")
        buf.write("!#\3\2\2\2\"\24\3\2\2\2\"\26\3\2\2\2\"\34\3\2\2\2\"\36")
        buf.write("\3\2\2\2#E\3\2\2\2$%\f\t\2\2%&\7\13\2\2&D\5\4\3\n\'(\f")
        buf.write("\b\2\2()\7\f\2\2)D\5\4\3\t*+\f\4\2\2+,\7\22\2\2,D\5\4")
        buf.write("\3\5-.\f\f\2\2.D\7\b\2\2/\60\f\13\2\2\60D\7\t\2\2\61\62")
        buf.write("\f\n\2\2\62D\7\n\2\2\63\64\f\7\2\2\64\65\7\r\2\2\65\66")
        buf.write("\7\16\2\2\66\67\7\30\2\2\67D\7\17\2\289\f\6\2\29:\7\r")
        buf.write("\2\2:;\7\20\2\2;<\7\30\2\2<D\7\17\2\2=>\f\5\2\2>?\7\r")
        buf.write("\2\2?@\7\30\2\2@A\7\21\2\2AB\7\30\2\2BD\7\17\2\2C$\3\2")
        buf.write("\2\2C\'\3\2\2\2C*\3\2\2\2C-\3\2\2\2C/\3\2\2\2C\61\3\2")
        buf.write("\2\2C\63\3\2\2\2C8\3\2\2\2C=\3\2\2\2DG\3\2\2\2EC\3\2\2")
        buf.write("\2EF\3\2\2\2F\5\3\2\2\2GE\3\2\2\2HM\5\b\5\2IJ\7\25\2\2")
        buf.write("JK\7\16\2\2KM\5\b\5\2LH\3\2\2\2LI\3\2\2\2M\7\3\2\2\2N")
        buf.write("V\t\2\2\2OP\t\2\2\2PQ\7\23\2\2QR\5\n\6\2RS\7\24\2\2SV")
        buf.write("\3\2\2\2TV\7\27\2\2UN\3\2\2\2UO\3\2\2\2UT\3\2\2\2V\t\3")
        buf.write("\2\2\2W\\\5\b\5\2XY\7\21\2\2Y[\5\b\5\2ZX\3\2\2\2[^\3\2")
        buf.write("\2\2\\Z\3\2\2\2\\]\3\2\2\2]\13\3\2\2\2^\\\3\2\2\2_d\7")
        buf.write("\25\2\2`a\7\21\2\2ac\7\25\2\2b`\3\2\2\2cf\3\2\2\2db\3")
        buf.write("\2\2\2de\3\2\2\2e\r\3\2\2\2fd\3\2\2\2\n\20\"CELU\\d")
        return buf.getvalue()


class RegExpParser ( Parser ):

    grammarFileName = "RegExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'exists'", "'{'", "'}'", "'~'", 
                     "'*'", "'+'", "'?'", "';'", "'&'", "'['", "'<='", "']'", 
                     "'>='", "','", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "TYPEDVAR", "CONSTANT", "NATURAL", "FLOATING", "WS" ]

    RULE_namedExpr = 0
    RULE_expr = 1
    RULE_binded_atom = 2
    RULE_atom = 3
    RULE_alist = 4
    RULE_idlist = 5

    ruleNames =  [ "namedExpr", "expr", "binded_atom", "atom", "alist", 
                   "idlist" ]

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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    IDENTIFIER=19
    TYPEDVAR=20
    CONSTANT=21
    NATURAL=22
    FLOATING=23
    WS=24

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
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return RegExpParser.RULE_namedExpr

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

        localctx = RegExpParser.NamedExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_namedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 12
                localctx.name = self.match(RegExpParser.IDENTIFIER)
                self.state = 13
                self.match(RegExpParser.T__0)


            self.state = 16
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
            return RegExpParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntersectionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntersection" ):
                listener.enterIntersection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntersection" ):
                listener.exitIntersection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntersection" ):
                return visitor.visitIntersection(self)
            else:
                return visitor.visitChildren(self)


    class AtomicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # Binded_atomContext
            self.copyFrom(ctx)

        def binded_atom(self):
            return self.getTypedRuleContext(RegExpParser.Binded_atomContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


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


    class UnionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExprContext,i)


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


    class ConcatenationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatenation" ):
                listener.enterConcatenation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatenation" ):
                listener.exitConcatenation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation" ):
                return visitor.visitConcatenation(self)
            else:
                return visitor.visitChildren(self)


    class StarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.args = None # IdlistContext
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def idlist(self):
            return self.getTypedRuleContext(RegExpParser.IdlistContext,0)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


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


    class RestrictGTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.l = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)

        def NATURAL(self):
            return self.getToken(RegExpParser.NATURAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestrictGT" ):
                listener.enterRestrictGT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestrictGT" ):
                listener.exitRestrictGT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestrictGT" ):
                return visitor.visitRestrictGT(self)
            else:
                return visitor.visitChildren(self)


    class RestrictContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.l = None # Token
            self.u = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)

        def NATURAL(self, i:int=None):
            if i is None:
                return self.getTokens(RegExpParser.NATURAL)
            else:
                return self.getToken(RegExpParser.NATURAL, i)

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


    class ComplementationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplementation" ):
                listener.enterComplementation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplementation" ):
                listener.exitComplementation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplementation" ):
                return visitor.visitComplementation(self)
            else:
                return visitor.visitChildren(self)


    class QuestionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


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


    class RestrictLTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.u = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)

        def NATURAL(self):
            return self.getToken(RegExpParser.NATURAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestrictLT" ):
                listener.enterRestrictLT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestrictLT" ):
                listener.exitRestrictLT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestrictLT" ):
                return visitor.visitRestrictLT(self)
            else:
                return visitor.visitChildren(self)


    class PlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegExpParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegExpParser.IDENTIFIER, RegExpParser.TYPEDVAR, RegExpParser.CONSTANT]:
                localctx = RegExpParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                localctx.child = self.binded_atom()
                pass
            elif token in [RegExpParser.T__1]:
                localctx = RegExpParser.ExistsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(RegExpParser.T__1)
                self.state = 21
                self.match(RegExpParser.T__2)
                self.state = 22
                localctx.args = self.idlist()
                self.state = 23
                self.match(RegExpParser.T__3)
                self.state = 24
                localctx.child = self.expr(12)
                pass
            elif token in [RegExpParser.T__4]:
                localctx = RegExpParser.ComplementationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(RegExpParser.T__4)
                self.state = 27
                localctx.child = self.expr(11)
                pass
            elif token in [RegExpParser.T__16]:
                localctx = RegExpParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(RegExpParser.T__16)
                self.state = 29
                localctx.child = self.expr(0)
                self.state = 30
                self.match(RegExpParser.T__17)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = RegExpParser.ConcatenationContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 35
                        self.match(RegExpParser.T__8)
                        self.state = 36
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = RegExpParser.IntersectionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        self.match(RegExpParser.T__9)
                        self.state = 39
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = RegExpParser.UnionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 41
                        self.match(RegExpParser.T__15)
                        self.state = 42
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = RegExpParser.StarContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 44
                        self.match(RegExpParser.T__5)
                        pass

                    elif la_ == 5:
                        localctx = RegExpParser.PlusContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 46
                        self.match(RegExpParser.T__6)
                        pass

                    elif la_ == 6:
                        localctx = RegExpParser.QuestionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 48
                        self.match(RegExpParser.T__7)
                        pass

                    elif la_ == 7:
                        localctx = RegExpParser.RestrictLTContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 50
                        self.match(RegExpParser.T__10)
                        self.state = 51
                        self.match(RegExpParser.T__11)
                        self.state = 52
                        localctx.u = self.match(RegExpParser.NATURAL)
                        self.state = 53
                        self.match(RegExpParser.T__12)
                        pass

                    elif la_ == 8:
                        localctx = RegExpParser.RestrictGTContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 55
                        self.match(RegExpParser.T__10)
                        self.state = 56
                        self.match(RegExpParser.T__13)
                        self.state = 57
                        localctx.l = self.match(RegExpParser.NATURAL)
                        self.state = 58
                        self.match(RegExpParser.T__12)
                        pass

                    elif la_ == 9:
                        localctx = RegExpParser.RestrictContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        self.match(RegExpParser.T__10)
                        self.state = 61
                        localctx.l = self.match(RegExpParser.NATURAL)
                        self.state = 62
                        self.match(RegExpParser.T__14)
                        self.state = 63
                        localctx.u = self.match(RegExpParser.NATURAL)
                        self.state = 64
                        self.match(RegExpParser.T__12)
                        pass

             
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Binded_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExpParser.RULE_binded_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarBindContext(Binded_atomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.Binded_atomContext
            super().__init__(parser)
            self.varname = None # Token
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)
        def atom(self):
            return self.getTypedRuleContext(RegExpParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarBind" ):
                listener.enterVarBind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarBind" ):
                listener.exitVarBind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarBind" ):
                return visitor.visitVarBind(self)
            else:
                return visitor.visitChildren(self)


    class VarConstContext(Binded_atomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.Binded_atomContext
            super().__init__(parser)
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(RegExpParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarConst" ):
                listener.enterVarConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarConst" ):
                listener.exitVarConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarConst" ):
                return visitor.visitVarConst(self)
            else:
                return visitor.visitChildren(self)



    def binded_atom(self):

        localctx = RegExpParser.Binded_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_binded_atom)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = RegExpParser.VarConstContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                localctx.child = self.atom()
                pass

            elif la_ == 2:
                localctx = RegExpParser.VarBindContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                localctx.varname = self.match(RegExpParser.IDENTIFIER)
                self.state = 72
                self.match(RegExpParser.T__11)
                self.state = 73
                localctx.child = self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExpParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def TYPEDVAR(self):
            return self.getToken(RegExpParser.TYPEDVAR, 0)
        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)

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


    class ConstantContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONSTANT(self):
            return self.getToken(RegExpParser.CONSTANT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.args = None # AlistContext
            self.copyFrom(ctx)

        def alist(self):
            return self.getTypedRuleContext(RegExpParser.AlistContext,0)

        def TYPEDVAR(self):
            return self.getToken(RegExpParser.TYPEDVAR, 0)
        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)

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

        localctx = RegExpParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = RegExpParser.PropContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                localctx.name = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RegExpParser.IDENTIFIER or _la==RegExpParser.TYPEDVAR):
                    localctx.name = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = RegExpParser.PredContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                localctx.name = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RegExpParser.IDENTIFIER or _la==RegExpParser.TYPEDVAR):
                    localctx.name = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 78
                self.match(RegExpParser.T__16)
                self.state = 79
                localctx.args = self.alist()
                self.state = 80
                self.match(RegExpParser.T__17)
                pass

            elif la_ == 3:
                localctx = RegExpParser.ConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(RegExpParser.CONSTANT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExpParser.RULE_alist

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomListContext(AlistContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.AlistContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.AtomContext)
            else:
                return self.getTypedRuleContext(RegExpParser.AtomContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomList" ):
                listener.enterAtomList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomList" ):
                listener.exitAtomList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomList" ):
                return visitor.visitAtomList(self)
            else:
                return visitor.visitChildren(self)



    def alist(self):

        localctx = RegExpParser.AlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alist)
        self._la = 0 # Token type
        try:
            localctx = RegExpParser.AtomListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.atom()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RegExpParser.T__14:
                self.state = 86
                self.match(RegExpParser.T__14)
                self.state = 87
                self.atom()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
                return self.getTokens(RegExpParser.IDENTIFIER)
            else:
                return self.getToken(RegExpParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return RegExpParser.RULE_idlist

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

        localctx = RegExpParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(RegExpParser.IDENTIFIER)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RegExpParser.T__14:
                self.state = 94
                self.match(RegExpParser.T__14)
                self.state = 95
                self.match(RegExpParser.IDENTIFIER)
                self.state = 100
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         




