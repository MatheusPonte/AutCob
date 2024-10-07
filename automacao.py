from playwright.sync_api import sync_playwright;
import time
from test import dado
import os

def Logar(username, password):
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False) #headless (debaixo dos panos)
        pagina = navegador.new_page()
    #Pagina do Site
        pagina.goto("https://app.cobmais.com.br/cob/pesquisa")
    #Login
        pagina.fill('xpath=//*[@id="Username"]', username)
    #Senha
        pagina.fill('xpath=//*[@id="Password"]', password)
    #Botão de entrar
        pagina.get_by_role('button').click()
        time.sleep(5);
    #Quadradin
        pagina.locator('xpath=//*[@id="menusuperior"]/a/i').click()
    #Clicando no quadrado
        pagina.locator('xpath=//*[@id="lkbCobranca"]').click()
#Area da cobrança
    #Estagio
        pagina.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/button').click()
        time.sleep(5)
        pagina.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/ul/li[3]/a/label').click()
        time.sleep(5)
        pagina.locator('xpath=//*[@id="divdadosContrato"]/div[4]/div/ul/li[4]/a/label/input').click()
        time.sleep(5)
    #Credor
        pagina.locator('xpath=//*[@id="divdadosContrato"]/div[1]/div/button').click()
        time.sleep(5);  
        pagina.locator('xpath=//*[@id="divdadosContrato"]/div[1]/div/ul/li[2]/a/label').click()
        pagina.locator('xpath=//*[@id="divdadosContrato"]/div[1]/div/ul/li[3]/a/label').click()
        #Clicando na area do nome
        # pagina.fill('xpath=//*[@id="txtNome"]',dado)
        # time.sleep(10)
    #pesquisar
        pagina.locator('xpath=//*[@id="btnPesquisar"]').click()
    #confirmar
        pagina.locator('xpath=//*[@id="btnConfirmaAtencao"]').click()
    #Selecionando a pessoa
        pagina.locator('xpath=//*[@id="tbCliente"]/tbody/tr[1]/td[10]/a').click()
    #Selecionando telefone
        pagina.locator('xpath=//*[@id="tbTelefone"]/tbody/tr[1]/td[4]/div/button').click()
        pagina.locator('xpath=//*[@id="tbTelefone"]/tbody/tr[1]/td[4]/div/ul/li[3]/a').click()
    #alternado wpp e autorizando
        pagina.locator('xpath=//*[@id="frmTelefone"]/fieldset/div/div[2]/div[2]/div/div[1]/label').click()
        pagina.locator('xpath=//*[@id="frmTelefone"]/fieldset/div/div[2]/div[3]/div/div[1]/label').click()
    #salvar
        pagina.locator('xpath=//*[@id="btnSalvarTelefone"]').click()

        time.sleep(5);  


Logar("",")

