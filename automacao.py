from playwright.sync_api import sync_playwright;
import time
from planilha import *

import os
import pyautogui as pya
from dotenv import load_dotenv
from tkinter import *
from tkinter import filedialog


count = 0
load_dotenv()
userw = os.getenv('USERN')
passw = os.getenv('PASSWORD')



def ler_contador():
    try:
        with open('contador.txt', 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0
def salvar_contador(valor):
    with open('contador.txt', 'w') as f:
        f.write(str(valor))

count = ler_contador()
def contador():
    count = count + 1
    print(count)


def Logar(p,username, password):
    #Pagina do Site
        p.goto("https://app.cobmais.com.br/cob/pesquisa")
    #Login
        p.fill('xpath=//*[@id="Username"]', username)
    #Senha
        p.fill('xpath=//*[@id="Password"]', password)
    #Botão de entrar
        p.get_by_role('button').click()
        time.sleep(5);

#------------------------------------------------------
def Pesquisar(p, nomes):
            #Quadradin
            p.locator('xpath=//*[@id="menusuperior"]/a/i').click()
    #Clicando no quadrado
            p.locator('xpath=//*[@id="lkbCobranca"]').click()
            #cookies
            if p.locator('xpath=//*[@id="beamerPushModal"]'):
                    p.locator('//*[@id="pushActionRefuse"]').click()
#Area da cobrança
#Estagio
            p.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/button').click()
            time.sleep(1)
            p.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/ul/li[3]/a/label').click()
            time.sleep(1)
            p.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/ul/li[4]/a/label/input').click()
            time.sleep(1)
            for nome in nomes:
                nome_str = str(nome)
                p.locator('xpath=//*[@id="txtCPFCNPJ"]').click()
#Clicando na area do nome
                p.fill('xpath=//*[@id="txtCPFCNPJ"]',nome_str)
                p.locator('xpath=//*[@id="txtCPFCNPJ"]').click()
                time.sleep(4)
 #pesquisar
                p.locator('xpath=//*[@id="btnPesquisar"]').click()
                time.sleep(4)
                usuario(p)
                


def obter_tamanho_tabela(p, xpath):
    # Obtendo o tamanho da tabela através do XPath
    linhas = p.locator(xpath)
    numero_de_linhas = linhas.count()
    print(f"Número de linhas na tabela: {numero_de_linhas}")
    return numero_de_linhas

#----------------
def usuario(p):        
        #Selecionando a pessoa
        p.locator('xpath=//*[@id="tbCliente"]/tbody/tr[1]/td[10]/a').click()
        #Selecionando telefone acao 1
        time.sleep(5)
        xpath_tabela = '//*[@id="tbTelefone"]/tbody/tr'
        tamanho_tabela = obter_tamanho_tabela(p, xpath_tabela)
        i = 0
        while i < tamanho_tabela:
            p.locator(f'xpath=//*[@id="tbTelefone"]/tbody/tr[{i+1}]/td[4]/div/button').click()
            try:
                   time.sleep(5)
                   img = pya.locateOnScreen('img/Alterar.png', confidence=0.8)
                   pya.click(img)
            except:
                   time.sleep(1)
        #alternado wpp e autorizando
            p.locator('xpath=//*[@id="frmTelefone"]/fieldset/div/div[2]/div[2]/div/div[1]/label').click()
            p.locator('xpath=//*[@id="frmTelefone"]/fieldset/div/div[2]/div[3]/div/div[1]/label').click()
        #salvar
            p.locator('xpath=//*[@id="btnSalvarTelefone"]').click()
            try:
                print('test no try')
                time.sleep(5)
                pya.locateOnScreen('img/AlertaAmarelo.png', confidence=0.7)
                p.locator('xpath=//*[@id="btnFecharTelefone"]').click()
                print('percorri o locate amarelo')
            except:
                   print('passei')
                   time.sleep(1)
            i = i + 1
            time.sleep(5)

        p.locator('xpath=//*[@id="btnVoltar"]').click()
        global count
        count += 1
        salvar_contador(count)
        print(f"Automação completada {count} vez(es).")


def rodar_automacao():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, args=["--start-maximized"])
        pagina = navegador.new_page()
        Logar(pagina, userw, passw)
        Pesquisar(pagina, nomes)
        usuario(pagina)
        contador()



janela = Tk()
janela.title("CobeMais")
text = Label(janela, text = "Automação Cobinho")
text.grid(column=0, row = 0)
button2 = Button(janela,text="Importar Planilha")
button2.grid(column=0,row=1)
button = Button(janela, text="Rodar automação", command= rodar_automacao)
button.grid(column=0,row=2)
janela.mainloop()

