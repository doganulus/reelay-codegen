# Generated from RegExp.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\7\f9\n\f\f\f\16\f<\13\f\3\r\6\r?\n\r\r\r\16")
        buf.write("\r@\3\r\3\r\3\16\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\2\35\2\3")
        buf.write("\2\5\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2G\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\37\3\2\2")
        buf.write("\2\5!\3\2\2\2\7&\3\2\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2")
        buf.write("\2\2\17.\3\2\2\2\21\60\3\2\2\2\23\62\3\2\2\2\25\64\3\2")
        buf.write("\2\2\27\66\3\2\2\2\31>\3\2\2\2\33D\3\2\2\2\35F\3\2\2\2")
        buf.write("\37 \7?\2\2 \4\3\2\2\2!\"\7V\2\2\"#\7t\2\2#$\7w\2\2$%")
        buf.write("\7g\2\2%\6\3\2\2\2&\'\7,\2\2\'\b\3\2\2\2()\7-\2\2)\n\3")
        buf.write("\2\2\2*+\7A\2\2+\f\3\2\2\2,-\7=\2\2-\16\3\2\2\2./\7~\2")
        buf.write("\2/\20\3\2\2\2\60\61\7*\2\2\61\22\3\2\2\2\62\63\7+\2\2")
        buf.write("\63\24\3\2\2\2\64\65\7.\2\2\65\26\3\2\2\2\66:\t\2\2\2")
        buf.write("\679\t\3\2\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2")
        buf.write(";\30\3\2\2\2<:\3\2\2\2=?\t\4\2\2>=\3\2\2\2?@\3\2\2\2@")
        buf.write(">\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\b\r\2\2C\32\3\2\2\2DE")
        buf.write("\4\62;\2E\34\3\2\2\2FG\4\63;\2G\36\3\2\2\2\5\2:@\3\2\3")
        buf.write("\2")
        return buf.getvalue()


class RegExpLexer(Lexer):

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
    IDENTIFIER = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'True'", "'*'", "'+'", "'?'", "';'", "'|'", "'('", "')'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "IDENTIFIER", "WS", "DIGIT", "DIGIT_NOT_ZERO" ]

    grammarFileName = "RegExp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


