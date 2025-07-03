# Generated from grammar/FormLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormLangParser import FormLangParser
else:
    from FormLangParser import FormLangParser

# This class defines a complete generic visitor for a parse tree produced by FormLangParser.

class FormLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormLangParser#program.
    def visitProgram(self, ctx:FormLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#form.
    def visitForm(self, ctx:FormLangParser.FormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#field.
    def visitField(self, ctx:FormLangParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#textField.
    def visitTextField(self, ctx:FormLangParser.TextFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#emailField.
    def visitEmailField(self, ctx:FormLangParser.EmailFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#numberField.
    def visitNumberField(self, ctx:FormLangParser.NumberFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#checkboxField.
    def visitCheckboxField(self, ctx:FormLangParser.CheckboxFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormLangParser#submitButton.
    def visitSubmitButton(self, ctx:FormLangParser.SubmitButtonContext):
        return self.visitChildren(ctx)



del FormLangParser