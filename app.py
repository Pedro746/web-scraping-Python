import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import json
import os

option = Options()
option.headless = True

# driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",options=option)
driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.set_window_size(2500,900)

url = "https://contratos.comprasnet.gov.br/transparencia/terceirizados?orgao=%5B%2244207%22%5D"

driver.get(url)



time.sleep(2)

# Clicando no botão de Visiblidade da Coluna
btn = "//button//span"
span_btn = driver.find_element_by_xpath(btn).click()

time.sleep(2)


# Selecionando o valor CUSTO na coluna
custo = '//div/ul/li[12]/a'
span_custo = driver.find_element_by_xpath(custo).click()

time.sleep(2)


# Selecionando o valor UNIDADE na coluna
unidade = '//div/ul/li[10]/a'
span_unidade = driver.find_element_by_xpath(unidade).click()

time.sleep(2)


# Selecionando o valor CPF na coluna
cpf = '//div/ul/li[5]/a'
span_cpf = driver.find_element_by_xpath(cpf).click()

time.sleep(2)


# Selecionando o valor SALÁRIO na coluna
salario = '//div/ul/li[11]/a'
span_salario = driver.find_element_by_xpath(salario).click()

time.sleep(2)



# Selecionar todos os valores 
span_xpath = "//select[@name='crudTable_length']//option[@value='-1']"
span_element = driver.find_element_by_xpath(span_xpath).click()

time.sleep(300)

#Selecionando a tabela
dados = driver.find_element_by_xpath("//div[@id='crudTable_wrapper']//div[@class='col-sm-12']")
html_content = dados.get_attribute('outerHTML')


# Parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(id='crudTable')

# Data Structure Conversion (Estruturar conteúdo em um Data Frame) - Pandas
df_full = pd.read_html(str(table))[0]
df = df_full[['Órgão', 'Unidade Gestora', 'Número Contrato', 'Nome', 'Função', 'Jornada', 'Unidade', 'Custo', 'Data Início', 'Situação']]
df.columns = ['Órgão', 'Unidade Gestora', 'Número Contrato', 'Nome', 'Função', 'Jornada', 'Unidade', 'Custo', 'Data Início', 'Situação']

print(df)
driver.quit()