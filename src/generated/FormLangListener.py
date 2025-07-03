# Generated from grammar/FormLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormLangParser import FormLangParser
else:
    from FormLangParser import FormLangParser

# This class defines a complete listener for a parse tree produced by FormLangParser.
class FormLangListener(ParseTreeListener):

    # Enter a parse tree produced by FormLangParser#program.
    def enterProgram(self, ctx:FormLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by FormLangParser#program.
    def exitProgram(self, ctx:FormLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by FormLangParser#form.
    def enterForm(self, ctx:FormLangParser.FormContext):
        pass

    # Exit a parse tree produced by FormLangParser#form.
    def exitForm(self, ctx:FormLangParser.FormContext):
        pass


    # Enter a parse tree produced by FormLangParser#field.
    def enterField(self, ctx:FormLangParser.FieldContext):
        pass

    # Exit a parse tree produced by FormLangParser#field.
    def exitField(self, ctx:FormLangParser.FieldContext):
        pass


    # Enter a parse tree produced by FormLangParser#textField.
    def enterTextField(self, ctx:FormLangParser.TextFieldContext):
        pass

    # Exit a parse tree produced by FormLangParser#textField.
    def exitTextField(self, ctx:FormLangParser.TextFieldContext):
        pass


    # Enter a parse tree produced by FormLangParser#emailField.
    def enterEmailField(self, ctx:FormLangParser.EmailFieldContext):
        pass

    # Exit a parse tree produced by FormLangParser#emailField.
    def exitEmailField(self, ctx:FormLangParser.EmailFieldContext):
        pass


    # Enter a parse tree produced by FormLangParser#numberField.
    def enterNumberField(self, ctx:FormLangParser.NumberFieldContext):
        pass

    # Exit a parse tree produced by FormLangParser#numberField.
    def exitNumberField(self, ctx:FormLangParser.NumberFieldContext):
        pass


    # Enter a parse tree produced by FormLangParser#checkboxField.
    def enterCheckboxField(self, ctx:FormLangParser.CheckboxFieldContext):
        pass

    # Exit a parse tree produced by FormLangParser#checkboxField.
    def exitCheckboxField(self, ctx:FormLangParser.CheckboxFieldContext):
        pass


    # Enter a parse tree produced by FormLangParser#submitButton.
    def enterSubmitButton(self, ctx:FormLangParser.SubmitButtonContext):
        pass

    # Exit a parse tree produced by FormLangParser#submitButton.
    def exitSubmitButton(self, ctx:FormLangParser.SubmitButtonContext):
        pass



del FormLangParser