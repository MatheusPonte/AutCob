from playwright.sync_api import sync_playwright;
import time
from test import dado
import os


     
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
def Pesquisar(p):
    #Quadradin
            p.locator('xpath=//*[@id="menusuperior"]/a/i').click()
    #Clicando no quadrado
            p.locator('xpath=//*[@id="lkbCobranca"]').click()
#Area da cobrança
    #Estagio
            p.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/button').click()
            time.sleep(5)
            p.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/ul/li[3]/a/label').click()
            time.sleep(5)
            p.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/ul/li[4]/a/label/input').click()
            time.sleep(5)
    #Credor
            p.locator('xpath=//*[@id="divdadosContrato"]/div[1]/div/button').click()
            time.sleep(5);  
            p.locator('xpath=//*[@id="divdadosContrato"]/div[1]/div/ul/li[2]/a/label').click()
            p.locator('xpath=//*[@id="divdadosContrato"]/div[1]/div/ul/li[3]/a/label').click()
            #Clicando na area do nome
            # p.fill('xpath=//*[@id="txtNome"]',dado)
            # time.sleep(10)
        #pesquisar
            p.locator('xpath=//*[@id="btnPesquisar"]').click()
        #confirmar caso aapareceça
            p.locator('xpath=//*[@id="btnConfirmaAtencao"]').click()

#----------------
def usuario(p):
        #Selecionando a pessoa
        p.locator('xpath=//*[@id="tbCliente"]/tbody/tr[1]/td[10]/a').click()
        #Selecionando telefone
        p.locator('xpath=//*[@id="tbTelefone"]/tbody/tr[1]/td[4]/div/button').click()
        p.locator('xpath=//*[@id="tbTelefone"]/tbody/tr[1]/td[4]/div/ul/li[3]/a').click()
        #alternado wpp e autorizando
        p.locator('xpath=//*[@id="frmTelefone"]/fieldset/div/div[2]/div[2]/div/div[1]/label').click()
        p.locator('xpath=//*[@id="frmTelefone"]/fieldset/div/div[2]/div[3]/div/div[1]/label').click()
        #salvar
        p.locator('xpath=//*[@id="btnSalvarTelefone"]').click()
        time.sleep(2);  
        p.locator('xpath=//*[@id="btnVoltar"]').click()

p = sync_playwright().start()
navegador = p.chromium.launch(headless=False) #headless (debaixo dos panos)
pagina = navegador.new_page()

Logar(pagina, "Victoria Ellen", "Meireles@2024")
Pesquisar(pagina)
usuario(pagina)