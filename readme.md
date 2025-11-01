# 🤖 Meu Primeiro Projeto de Automação com Python

Este é um projeto de estudos que criei para praticar Python e a biblioteca Pandas.

O objetivo era aprender como automatizar uma tarefa que eu costumava fazer manualmente no Excel.

## 🎯 O Desafio

No meu trabalho e em cursos, eu vi que muitas vezes precisamos juntar informações de planilhas diferentes.

Neste projeto, eu imaginei um cenário com duas planilhas:
1.  `funcionarios.xlsx`: Uma lista de funcionários.
2.  `absenteismo.xlsx`: Uma lista de faltas.

O desafio era: como eu posso criar um terceiro relatório, juntando as informações dessas duas planilhas, sem ter que usar `PROCV` (VLOOKUP) no Excel manualmente?

## 🚀 A Solução com Python

Eu usei o Python para criar um script que faz todo o trabalho pesado:

1.  O script lê os dois arquivos (`funcionarios.xlsx` e `absenteismo.xlsx`).
2.  Ele usa a biblioteca **Pandas** para "cruzar" as informações, usando o ID do funcionário como chave.
3.  Depois de juntar tudo, ele limpa os dados e organiza as colunas.
4.  No final, ele salva um **novo arquivo** chamado `relatorio_consolidado.xlsx`, já com tudo pronto!

## 🛠️ O que eu Usei (e Aprendi)

* **Python:** A linguagem de programação.
* **Pandas:** A principal biblioteca que usei. Aprendi a usar o `pd.read_excel` (para ler), o `pd.merge` (para juntar) e o `pd.to_excel` (para salvar).
* **OpenPyXL:** A ferramenta que o Pandas usa por baixo dos panos para funcionar com arquivos `.xlsx`.
* **Ambiente Virtual (`venv`):** Aprendi a criar um ambiente separado para instalar as bibliotecas do projeto, o que é uma boa prática.

## 🏁 Como Executar

Se você quiser testar meu script, estes são os passos:

1.  **Clone este repositório.**
2.  **Abra o terminal** na pasta do projeto.
3.  **Crie e ative um ambiente virtual:**
    * `python -m venv venv`
    * `venv\Scripts\activate` (no Windows)
4.  **Instale o que precisa:**
    * `pip install pandas openpyxl`
5.  **Rode o script:**
    * `python main.py`

E pronto! O script vai criar o arquivo `relatorio_consolidado.xlsx` para você.