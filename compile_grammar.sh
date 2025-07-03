java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor grammar/FormLang.g4 -o src/generated
touch src/generated/__init__.py
