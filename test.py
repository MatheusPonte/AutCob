import pandas

arquivo_excel = 'BASE DE DEVEDORES EXTRAJUDICIAL.xlsx'

# Carregar a planilha em um DataFrame
df = pandas.read_excel(arquivo_excel, dtype={'CPF/CNPJ': str})

# Acessar a coluna "nome" e armazenar em um array (lista)
nomes = df['CPF/CNPJ'].tolist()
# dado = df.loc["CPF/CNPJ"]

# Exibir os nomes armazenados
    # print(len(nomes))