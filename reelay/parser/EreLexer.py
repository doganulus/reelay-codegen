# Generated from Ere.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\7\r<\n\r\f\r\16\r?\13\r\3\16")
        buf.write("\3\16\3\16\6\16D\n\16\r\16\16\16E\5\16H\n\16\3\17\6\17")
        buf.write("K\n\17\r\17\16\17L\3\17\3\17\3\20\3\20\3\21\3\21\2\2\22")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\2!\2\3\2\5\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\5\2\13\f\17\17\"\"\2U\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3#\3\2\2\2\5%")
        buf.write("\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2")
        buf.write("\17/\3\2\2\2\21\61\3\2\2\2\23\63\3\2\2\2\25\65\3\2\2\2")
        buf.write("\27\67\3\2\2\2\319\3\2\2\2\33G\3\2\2\2\35J\3\2\2\2\37")
        buf.write("P\3\2\2\2!R\3\2\2\2#$\7\u0080\2\2$\4\3\2\2\2%&\7\'\2\2")
        buf.write("&\6\3\2\2\2\'(\7*\2\2(\b\3\2\2\2)*\7.\2\2*\n\3\2\2\2+")
        buf.write(",\7+\2\2,\f\3\2\2\2-.\7(\2\2.\16\3\2\2\2/\60\7,\2\2\60")
        buf.write("\20\3\2\2\2\61\62\7-\2\2\62\22\3\2\2\2\63\64\7A\2\2\64")
        buf.write("\24\3\2\2\2\65\66\7=\2\2\66\26\3\2\2\2\678\7~\2\28\30")
        buf.write("\3\2\2\29=\t\2\2\2:<\t\3\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2")
        buf.write("\2\2=>\3\2\2\2>\32\3\2\2\2?=\3\2\2\2@H\5\37\20\2AC\5!")
        buf.write("\21\2BD\5\37\20\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2")
        buf.write("\2\2FH\3\2\2\2G@\3\2\2\2GA\3\2\2\2H\34\3\2\2\2IK\t\4\2")
        buf.write("\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MN\3\2\2\2N")
        buf.write("O\b\17\2\2O\36\3\2\2\2PQ\4\62;\2Q \3\2\2\2RS\4\63;\2S")
        buf.write("\"\3\2\2\2\7\2=EGL\3\2\3\2")
        return buf.getvalue()


class EreLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    IDENTIFIER = 12
    NUMBER = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'~'", "'%'", "'('", "','", "')'", "'&'", "'*'", "'+'", "'?'", 
            "';'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "IDENTIFIER", "NUMBER", 
                  "WS", "DIGIT", "DIGIT_NOT_ZERO" ]

    grammarFileName = "Ere.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


