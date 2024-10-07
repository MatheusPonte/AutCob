import pandas

arquivo_excel = 'BASE DE DEVEDORES EXTRAJUDICIAL.xlsx'

# Carregar a planilha em um DataFrame
df = pandas.read_excel(arquivo_excel)

# Acessar a coluna "nome" e armazenar em um array (lista)
nomes = df['CLIENTE'].tolist()
dado = df.loc[0, "CLIENTE"]

# Exibir os nomes armazenados
    # print(len(nomes))