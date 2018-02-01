# Generated from Ere.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\7")
        buf.write("\20M\n\20\f\20\16\20P\13\20\3\21\3\21\3\21\6\21U\n\21")
        buf.write("\r\21\16\21V\5\21Y\n\21\3\22\6\22\\\n\22\r\22\16\22]\3")
        buf.write("\22\3\22\3\23\3\23\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\2\'\2\3\2\5\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\2f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\3)\3\2\2\2\5\60\3\2\2\2\7\62\3\2\2\2\t\64")
        buf.write("\3\2\2\2\13\66\3\2\2\2\r8\3\2\2\2\17:\3\2\2\2\21<\3\2")
        buf.write("\2\2\23>\3\2\2\2\25@\3\2\2\2\27B\3\2\2\2\31D\3\2\2\2\33")
        buf.write("F\3\2\2\2\35H\3\2\2\2\37J\3\2\2\2!X\3\2\2\2#[\3\2\2\2")
        buf.write("%a\3\2\2\2\'c\3\2\2\2)*\7g\2\2*+\7z\2\2+,\7k\2\2,-\7u")
        buf.write("\2\2-.\7v\2\2./\7u\2\2/\4\3\2\2\2\60\61\7\60\2\2\61\6")
        buf.write("\3\2\2\2\62\63\7\u0080\2\2\63\b\3\2\2\2\64\65\7}\2\2\65")
        buf.write("\n\3\2\2\2\66\67\7.\2\2\67\f\3\2\2\289\7\177\2\29\16\3")
        buf.write("\2\2\2:;\7(\2\2;\20\3\2\2\2<=\7,\2\2=\22\3\2\2\2>?\7-")
        buf.write("\2\2?\24\3\2\2\2@A\7A\2\2A\26\3\2\2\2BC\7=\2\2C\30\3\2")
        buf.write("\2\2DE\7~\2\2E\32\3\2\2\2FG\7*\2\2G\34\3\2\2\2HI\7+\2")
        buf.write("\2I\36\3\2\2\2JN\t\2\2\2KM\t\3\2\2LK\3\2\2\2MP\3\2\2\2")
        buf.write("NL\3\2\2\2NO\3\2\2\2O \3\2\2\2PN\3\2\2\2QY\5%\23\2RT\5")
        buf.write("\'\24\2SU\5%\23\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2")
        buf.write("\2\2WY\3\2\2\2XQ\3\2\2\2XR\3\2\2\2Y\"\3\2\2\2Z\\\t\4\2")
        buf.write("\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2")
        buf.write("_`\b\22\2\2`$\3\2\2\2ab\4\62;\2b&\3\2\2\2cd\4\63;\2d(")
        buf.write("\3\2\2\2\7\2NVX]\3\2\3\2")
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
    T__11 = 12
    T__12 = 13
    T__13 = 14
    IDENTIFIER = 15
    NUMBER = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'exists'", "'.'", "'~'", "'{'", "','", "'}'", "'&'", "'*'", 
            "'+'", "'?'", "';'", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "IDENTIFIER", "NUMBER", "WS", "DIGIT", "DIGIT_NOT_ZERO" ]

    grammarFileName = "Ere.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


