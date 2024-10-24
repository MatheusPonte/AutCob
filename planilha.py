import pandas

arquivo_excel = 'BASE DE DEVEDORES EXTRAJUDICIAL.xlsx'
arquivo_excel2 = 'Pasta1.xlsx'

# Carregar a planilha em um DataFrame
df2 = pandas.read_excel(arquivo_excel2)
df = pandas.read_excel(arquivo_excel,dtype={'CPF/CNPJ': str})

# Acessar a coluna "nome" e armazenar em um array (lista)
nomes = df['CPF/CNPJ'].tolist()
concluido = df['Status'].tolist()
# dado = df.loc["CPF/CNPJ"]