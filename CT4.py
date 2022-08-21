from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

link = 'https://cadastramento-demo.mercafacil.com/#/home'
cnpj = '15.415.809/0001-51'
razao_social = 'Débora e Maya Joalheria ME'
celular = '(62) 98751-7969'
tel_contato = '(62) 3568-7729'
email = 'financeiro@deboraemayajoalheriame.com.br'
cep = '74483-410'
numero = '45'
senha = '123456'
confirma_senha = senha


# Acessando a pagina de cadastro CNPJ

nav = webdriver.Chrome()
nav.get(link)
nav.maximize_window()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/section/div/div[2]/button').click()
sleep(3)
nav.find_element(By.ID,'input-19').send_keys(cnpj)
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div[2]/div/div/div[2]/button').click()
sleep(3)

# Inserindo dados para o cadastramento

nav.find_element(By.ID,'input-46').send_keys(razao_social)
sleep(2)
nav.find_element(By.ID,'input-50').send_keys(celular)
sleep(2)
nav.find_element(By.ID,'input-54').send_keys(tel_contato)
sleep(2)
nav.find_element(By.ID,'input-58').send_keys(email)
sleep(2)
nav.find_element(By.ID,'input-75').send_keys(cep)
sleep(2)
nav.find_element(By.ID,'input-102').send_keys(numero)
sleep(2)
nav.find_element(By.ID,'input-62').send_keys(senha)
sleep(2)
nav.find_element(By.ID,'input-66').send_keys(confirma_senha)
sleep(2)

# marcando os termos de adesão

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[9]/div[1]').click()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div/div/div[2]/button[1]').click()
sleep(3)
nav.find_element(By.ID,'input-66').send_keys(Keys.PAGE_DOWN)
sleep(2)

# Confirmando o cadastro

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[9]/div[2]/button[1]').click()
sleep(2)
nav.delete_all_cookies()
sleep(3)
nav.close()

