# Passo 1: Importar a biblioteca pandas (nossa ferramenta de análise)
import pandas as pd

print("Iniciando o script de automação...")

try:
    # Passo 2: Carregar os arquivos Excel para dentro do Python
    # Nós instalamos 'openpyxl' para que esta linha funcione
    df_funcionarios = pd.read_excel('funcionarios.xlsx')
    df_absenteismo = pd.read_excel('absenteismo.xlsx')

    print("Arquivos 'funcionarios.xlsx' e 'absenteismo.xlsx' carregados.")
    
    # OPCIONAL: Verifique os dados (descomente as linhas abaixo para ver)
    # print("--- Dados Funcionários ---")
    # print(df_funcionarios.head()) # .head() mostra os 5 primeiros
    # print("--- Dados Absenteísmo ---")
    # print(df_absenteismo.head())


    # Passo 3: A Mágica! (O "PROCV")
    # Vamos "mesclar" (merge) as duas tabelas.
    df_consolidado = pd.merge(
        df_absenteismo,                 # Tabela da esquerda (a principal)
        df_funcionarios,                # Tabela da direita (a que vamos buscar info)
        left_on='ID_Func',              # Chave da tabela da esquerda
        right_on='ID',                  # Chave da tabela da direita
        how='left'                      # 'how=left' garante que manteremos todas as faltas
    )

    print("Dados consolidados com sucesso.")

    # Passo 4: Limpando o relatório
    # O merge cria duas colunas de ID ('ID_Func' e 'ID'). Vamos remover a extra.
    df_consolidado = df_consolidado.drop(columns=['ID'])

    # Vamos reordenar as colunas para ficar mais legível para o gestor
    colunas_ordenadas = ['Data', 'Nome', 'Departamento', 'Horas_Faltas', 'ID_Func']
    df_consolidado = df_consolidado[colunas_ordenadas]

    # Passo 5: Salvar o resultado em um novo arquivo Excel
    # 'index=False' é importante para não salvar um índice inútil do Pandas na planilha
    nome_arquivo_saida = 'relatorio_consolidado.xlsx'
    df_consolidado.to_excel(nome_arquivo_saida, index=False)

    # len(df_consolidado) vai contar quantas linhas seu relatório final tem (150)
    print(f"Relatório final com {len(df_consolidado)} registros salvo como '{nome_arquivo_saida}'!")

except FileNotFoundError:
    print("ERRO: Verifique se os arquivos 'funcionarios.xlsx' e 'absenteismo.xlsx' estão na mesma pasta do script.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")