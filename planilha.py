import pandas
from tkinter import filedialog
from automacao import *



arquivo_excel = filedialog.askopenfilename(title="Selecione o arquivo BASE DE DEVEDORES", filetypes=[("Arquivos Excel", "*.xlsx *.xls")])


df = pandas.read_excel(arquivo_excel,dtype={'CPF/CNPJ': str})

# Acessar a coluna "nome" e armazenar em um array (lista)
nomes = df['CPF/CNPJ'].tolist()
concluido = df['Status'].tolist()