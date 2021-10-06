# Atividade Final Compiladores 1

Implementação da parte frontend do compilador, ou seja até a geração de código intermédiário.
Pode ser em qualquer linguagem.
Não pode usar bibliotecas que façam a tokenização, nem as análises sintáticas e semânticas.
Pode ser qualquer análise sintática, top-down ou bottom-up.
Deverá estar em algum versionamento de código (github, gitlab, etc)
# Deverá ser entregue:
- Automato do analisador léxico
- A gramática com as regras semânticas
- Código fonte do programa

# Lexico.py
Classe Lex implementa o analisador léxico, com métodos de tokenização. Diagrama das regras na pasta /diagramas

# Sintatico.py
Classe Sintatico implementa analise sintatica da linguagem, com os metodos das regras de produção e controla o analisador léxico.

# Semantico.py
Em produção...



# Detalhes:
1. A regra de atribuição foi alterada de (:=) para (=)
2. O arquivo teste.txt fornecido no na tarefa possui erros sintaticos, para teste usar o arquivo CORRETO_teste.txt, ambos em /Exmeplos
