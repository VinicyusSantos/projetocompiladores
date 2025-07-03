# 📝 FormLang

## 👥 Equipe

- Vinicyus Santos  

---

## 🎯 Motivação

Durante estágios e projetos web, desenvolvedores frequentemente precisam criar formulários HTML para coletar dados de usuários. No entanto, essa tarefa pode ser repetitiva, propensa a erros e exigir conhecimento de HTML/CSS.

**FormLang** resolve esse problema ao permitir que o desenvolvedor descreva formulários de forma simples e legível, com uma linguagem própria. A saída da linguagem é um arquivo HTML pronto para ser usado.

---

## 💡 Descrição da Linguagem

A linguagem possui um único bloco principal: `form "<Título>"`, que contém instruções de criação de campos.

### Componentes suportados:

| Comando          | Resultado HTML                     |
|------------------|------------------------------------|
| `text "Nome"`    | `<input type="text">`              |
| `email "Email"`  | `<input type="email">`             |
| `number "Idade"` | `<input type="number">`            |
| `checkbox "..."` | `<input type="checkbox">`          |
| `submit "..."`   | `<button type="submit">`           |

---

## 📄 Exemplo de Programa

### Entrada (`cadastro.formlang`):

```formlang
form "Cadastro de Usuário" {
    text "Nome"
    email "Email"
    number "Idade"
    checkbox "Aceita os termos?"
    submit "Cadastrar"
}
```

### Saída esperada (`form.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
</head>
<body>
    <h1>Cadastro de Usuário</h1>
    <form>
        <label>Nome</label><br>
        <input type="text"><br><br>

        <label>Email</label><br>
        <input type="email"><br><br>

        <label>Idade</label><br>
        <input type="number"><br><br>

        <label>Aceita os termos?</label>
        <input type="checkbox"><br><br>

        <button type="submit">Cadastrar</button>
    </form>
</body>
</html>
```

---

## 🚀 Como Executar

### ✅ Opção 1: Usando GitHub Codespaces (recomendado)

1. Abra o projeto no GitHub.
2. Clique em **`<> Code` → `Codespaces` → `Create codespace on main`**.
3. O ambiente será configurado automaticamente com:
   - Python 3
   - Java JDK
   - ANTLR
4. No terminal integrado, execute:

```bash
antlr4 -Dlanguage=Python3 grammar/FormLang.g4 -o src/generated
python src/formlang.py examples/cadastro.formlang
```

### 💻 Opção 2: Executando localmente

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/formlang.git
cd formlang
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Compile a gramática:

```bash
antlr4 -Dlanguage=Python3 grammar/FormLang.g4 -o src/generated
```

4. Execute o interpretador:

```bash
python src/formlang.py examples/cadastro.formlang
```

---

## 📁 Estrutura do Projeto

```
formlang/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── grammar/
│   └── FormLang.g4
├── src/
│   ├── formlang.py
│   ├── generator.py
│   ├── ast.py
│   └── generated/
├── examples/
│   └── cadastro.formlang
├── tests/
│   └── test_generator.py
├── requirements.txt
├── compile_grammar.sh
└── README.md
```

---

## 🧪 Testes

```bash
pytest
```

---

## 🧠 Implementação

- **Lexer/Parser** gerado com ANTLR
- **AST** construída com classes em Python
- **Interpretador** converte AST em HTML
- **Semântica** verifica campos duplicados

---
