# Projeto de Automação de Planilhas com Python

Este projeto foi criado para praticar Python e a biblioteca Pandas. O objetivo é automatizar a tarefa de juntar informações de duas planilhas diferentes de forma rápida e organizada.

## Descrição do Desafio

O script resolve um problema comum: unir dados de fontes distintas. No exemplo utilizado, temos dois arquivos:
* **funcionarios.xlsx**: Contém a lista de funcionários.
* **absenteismo.xlsx**: Contém a lista de faltas.

O script lê esses arquivos e cria um terceiro relatório consolidado, automatizando o que seria feito manualmente com funções como o PROCV no Excel.

## Ferramentas Utilizadas

* **Python**: Linguagem de programação base.
* **Pandas**: Biblioteca para manipulação e análise de dados.
* **OpenPyXL**: Biblioteca para leitura e escrita de arquivos Excel.

## Como Funciona

1. O script carrega os dados das duas planilhas.
2. Utiliza o ID do funcionário para cruzar as informações.
3. Organiza as colunas e limpa os dados.
4. Exporta o resultado para um novo arquivo chamado **relatorio_consolidado.xlsx**.

## Passo a Passo para Executar

Para rodar o projeto na sua máquina, siga estas etapas no terminal:

1. **Clonar o repositório** para o seu computador.
2. **Criar um ambiente virtual** para manter as bibliotecas organizadas:
   python -m venv venv
3. **Ativar o ambiente virtual**:
   - No Windows: `venv\Scripts\activate`
   - No Mac/Linux: `source venv/bin/activate`
4. **Instalar as dependências**:
   pip install pandas openpyxl
5. **Rodar o script**:
   python main.py

Após seguir esses passos, o novo arquivo Excel será gerado na pasta do projeto.
