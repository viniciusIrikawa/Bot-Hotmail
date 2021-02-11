from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\chromedriver')    # You need to install the 'chromedriver'

def logar():
    id_login = 'i0116'
    id_button = 'idSIButton9'
    id_pass = 'i0118'
    id_entrar = 'idSIButton9'
    id_opcao = 'idBtn_Back'
    login = ' '              # Insert your login
    password = ' '           # Insert your password
    driver.get('https://login.live.com/')

    login_field = driver.find_element_by_id(id_login)
    login_field.send_keys(login)                             # Fill in the login field
    sleep(2)
    btn_1 = driver.find_element_by_id(id_button)             # Click on the button
    btn_1.click()
    password_field = driver.find_element_by_id(id_pass)
    password_field.send_keys(password)                       # Fill in the password field
    sleep(2)
    btn_2 = driver.find_element_by_id(id_entrar)             # Click on the 'confirm' button
    btn_2.click()
    opcao_nao = driver.find_element_by_id(id_opcao)
    sleep(2)
    opcao_nao.click()
logar()

