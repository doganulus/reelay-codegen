# Generated from PastLTL.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\7\17U\n\17\f\17\16\17X\13")
        buf.write("\17\3\20\6\20[\n\20\r\20\16\20\\\3\20\3\20\3\21\3\21\3")
        buf.write("\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\2#\2\3\2\5\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2c\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2")
        buf.write("\t-\3\2\2\2\13\60\3\2\2\2\r\64\3\2\2\2\17\67\3\2\2\2\21")
        buf.write(":\3\2\2\2\23?\3\2\2\2\25F\3\2\2\2\27L\3\2\2\2\31N\3\2")
        buf.write("\2\2\33P\3\2\2\2\35R\3\2\2\2\37Z\3\2\2\2!`\3\2\2\2#b\3")
        buf.write("\2\2\2%&\7?\2\2&\4\3\2\2\2\'(\7#\2\2(\6\3\2\2\2)*\7p\2")
        buf.write("\2*+\7q\2\2+,\7v\2\2,\b\3\2\2\2-.\7(\2\2./\7(\2\2/\n\3")
        buf.write("\2\2\2\60\61\7c\2\2\61\62\7p\2\2\62\63\7f\2\2\63\f\3\2")
        buf.write("\2\2\64\65\7~\2\2\65\66\7~\2\2\66\16\3\2\2\2\678\7q\2")
        buf.write("\289\7t\2\29\20\3\2\2\2:;\7q\2\2;<\7p\2\2<=\7e\2\2=>\7")
        buf.write("g\2\2>\22\3\2\2\2?@\7c\2\2@A\7n\2\2AB\7y\2\2BC\7c\2\2")
        buf.write("CD\7{\2\2DE\7u\2\2E\24\3\2\2\2FG\7u\2\2GH\7k\2\2HI\7p")
        buf.write("\2\2IJ\7e\2\2JK\7g\2\2K\26\3\2\2\2LM\7*\2\2M\30\3\2\2")
        buf.write("\2NO\7+\2\2O\32\3\2\2\2PQ\7.\2\2Q\34\3\2\2\2RV\t\2\2\2")
        buf.write("SU\t\3\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\36")
        buf.write("\3\2\2\2XV\3\2\2\2Y[\t\4\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3")
        buf.write("\2\2\2\\]\3\2\2\2]^\3\2\2\2^_\b\20\2\2_ \3\2\2\2`a\4\62")
        buf.write(";\2a\"\3\2\2\2bc\4\63;\2c$\3\2\2\2\5\2V\\\3\2\3\2")
        return buf.getvalue()


class PastLTLLexer(Lexer):

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
    IDENTIFIER = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'!'", "'not'", "'&&'", "'and'", "'||'", "'or'", "'once'", 
            "'always'", "'since'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "IDENTIFIER", 
                  "WS", "DIGIT", "DIGIT_NOT_ZERO" ]

    grammarFileName = "PastLTL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


