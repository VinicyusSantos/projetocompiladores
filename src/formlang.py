import sys
from antlr4 import *
from generated.FormLangLexer import FormLangLexer
from generated.FormLangParser import FormLangParser
from ast import Form, Field
from generator import generate_html
from generated.FormLangVisitor import FormLangVisitor as BaseVisitor
from generated.FormLangVisitor import FormLangVisitor as BaseVisitor

class FormLangVisitor(ParseTreeVisitor):
    def visitProgram(self, ctx):
        print("visitProgram chamado")
        return self.visit(ctx.form())

    def visitForm(self, ctx):
        title = ctx.STRING().getText().strip('"')
        print(f"visitForm: title = {title}")
        fields = [self.visit(f) for f in ctx.field()]
        print(f"visitForm: campos encontrados = {len(fields)}")
        return Form(title, fields)

    def visitTextField(self, ctx):
        label = ctx.STRING().getText().strip('"')
        print(f"visitTextField: {label}")
        return Field('text', label)

    def visitEmailField(self, ctx):
        label = ctx.STRING().getText().strip('"')
        print(f"visitEmailField: {label}")
        return Field('email', label)

    def visitNumberField(self, ctx):
        label = ctx.STRING().getText().strip('"')
        print(f"visitNumberField: {label}")
        return Field('number', label)

    def visitCheckboxField(self, ctx):
        label = ctx.STRING().getText().strip('"')
        print(f"visitCheckboxField: {label}")
        return Field('checkbox', label)

    def visitSubmitButton(self, ctx):
        label = ctx.STRING().getText().strip('"')
        print(f"visitSubmitButton: {label}")
        return Field('submit', label)


def main():
    if len(sys.argv) < 2:
        print("Uso: python formlang.py <arquivo.formlang>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        input_stream = InputStream(f.read())

    lexer = FormLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FormLangParser(stream)
    tree = parser.program()

    visitor = FormLangVisitor()
    form_ast = visitor.visit(tree)

    html = generate_html(form_ast)
    with open("form.html", "w") as f:
        f.write(html)
    print("✅ Formulário gerado: form.html")

if __name__ == "__main__":
    main()
