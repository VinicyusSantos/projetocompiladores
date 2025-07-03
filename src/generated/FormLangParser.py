# Generated from grammar/FormLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,4,1,4,1,4,
        1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,
        0,0,49,0,16,1,0,0,0,2,19,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,8,40,
        1,0,0,0,10,43,1,0,0,0,12,46,1,0,0,0,14,49,1,0,0,0,16,17,3,2,1,0,
        17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,9,0,0,21,25,5,2,
        0,0,22,24,3,4,2,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,3,0,0,29,3,1,0,0,0,30,
        36,3,6,3,0,31,36,3,8,4,0,32,36,3,10,5,0,33,36,3,12,6,0,34,36,3,14,
        7,0,35,30,1,0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,
        1,0,0,0,36,5,1,0,0,0,37,38,5,4,0,0,38,39,5,9,0,0,39,7,1,0,0,0,40,
        41,5,5,0,0,41,42,5,9,0,0,42,9,1,0,0,0,43,44,5,6,0,0,44,45,5,9,0,
        0,45,11,1,0,0,0,46,47,5,7,0,0,47,48,5,9,0,0,48,13,1,0,0,0,49,50,
        5,8,0,0,50,51,5,9,0,0,51,15,1,0,0,0,2,25,35
    ]

class FormLangParser ( Parser ):

    grammarFileName = "FormLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'form'", "'{'", "'}'", "'text'", "'email'", 
                     "'number'", "'checkbox'", "'submit'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "WS" ]

    RULE_program = 0
    RULE_form = 1
    RULE_field = 2
    RULE_textField = 3
    RULE_emailField = 4
    RULE_numberField = 5
    RULE_checkboxField = 6
    RULE_submitButton = 7

    ruleNames =  [ "program", "form", "field", "textField", "emailField", 
                   "numberField", "checkboxField", "submitButton" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    STRING=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(FormLangParser.FormContext,0)


        def EOF(self):
            return self.getToken(FormLangParser.EOF, 0)

        def getRuleIndex(self):
            return FormLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FormLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.form()
            self.state = 17
            self.match(FormLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormLangParser.STRING, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormLangParser.FieldContext)
            else:
                return self.getTypedRuleContext(FormLangParser.FieldContext,i)


        def getRuleIndex(self):
            return FormLangParser.RULE_form

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForm" ):
                listener.enterForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForm" ):
                listener.exitForm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForm" ):
                return visitor.visitForm(self)
            else:
                return visitor.visitChildren(self)




    def form(self):

        localctx = FormLangParser.FormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_form)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(FormLangParser.T__0)
            self.state = 20
            self.match(FormLangParser.STRING)
            self.state = 21
            self.match(FormLangParser.T__1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 496) != 0):
                self.state = 22
                self.field()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(FormLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textField(self):
            return self.getTypedRuleContext(FormLangParser.TextFieldContext,0)


        def emailField(self):
            return self.getTypedRuleContext(FormLangParser.EmailFieldContext,0)


        def numberField(self):
            return self.getTypedRuleContext(FormLangParser.NumberFieldContext,0)


        def checkboxField(self):
            return self.getTypedRuleContext(FormLangParser.CheckboxFieldContext,0)


        def submitButton(self):
            return self.getTypedRuleContext(FormLangParser.SubmitButtonContext,0)


        def getRuleIndex(self):
            return FormLangParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = FormLangParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_field)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.textField()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.emailField()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.numberField()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.checkboxField()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.submitButton()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormLangParser.STRING, 0)

        def getRuleIndex(self):
            return FormLangParser.RULE_textField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextField" ):
                listener.enterTextField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextField" ):
                listener.exitTextField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextField" ):
                return visitor.visitTextField(self)
            else:
                return visitor.visitChildren(self)




    def textField(self):

        localctx = FormLangParser.TextFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_textField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(FormLangParser.T__3)
            self.state = 38
            self.match(FormLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmailFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormLangParser.STRING, 0)

        def getRuleIndex(self):
            return FormLangParser.RULE_emailField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmailField" ):
                listener.enterEmailField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmailField" ):
                listener.exitEmailField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmailField" ):
                return visitor.visitEmailField(self)
            else:
                return visitor.visitChildren(self)




    def emailField(self):

        localctx = FormLangParser.EmailFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_emailField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(FormLangParser.T__4)
            self.state = 41
            self.match(FormLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormLangParser.STRING, 0)

        def getRuleIndex(self):
            return FormLangParser.RULE_numberField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberField" ):
                listener.enterNumberField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberField" ):
                listener.exitNumberField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberField" ):
                return visitor.visitNumberField(self)
            else:
                return visitor.visitChildren(self)




    def numberField(self):

        localctx = FormLangParser.NumberFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numberField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(FormLangParser.T__5)
            self.state = 44
            self.match(FormLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckboxFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormLangParser.STRING, 0)

        def getRuleIndex(self):
            return FormLangParser.RULE_checkboxField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckboxField" ):
                listener.enterCheckboxField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckboxField" ):
                listener.exitCheckboxField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckboxField" ):
                return visitor.visitCheckboxField(self)
            else:
                return visitor.visitChildren(self)




    def checkboxField(self):

        localctx = FormLangParser.CheckboxFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_checkboxField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(FormLangParser.T__6)
            self.state = 47
            self.match(FormLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubmitButtonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormLangParser.STRING, 0)

        def getRuleIndex(self):
            return FormLangParser.RULE_submitButton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubmitButton" ):
                listener.enterSubmitButton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubmitButton" ):
                listener.exitSubmitButton(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubmitButton" ):
                return visitor.visitSubmitButton(self)
            else:
                return visitor.visitChildren(self)




    def submitButton(self):

        localctx = FormLangParser.SubmitButtonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_submitButton)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(FormLangParser.T__7)
            self.state = 50
            self.match(FormLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





