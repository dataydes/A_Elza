# -*- coding: utf-8 -*-
from logging import error
import sys #coleta o link
import time #tempo de espera da url
from urllib import request, parse
from warnings import catch_warnings #biblioteca da url
from selenium import webdriver #Coleta o nome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime #define a hora
import os #comando para o shell

def finalizar():
	driver.close()
	driver.quit()
	return None

arg = sys.argv[1] #Recupera a variável de entrada
print ("Coletando o nome do vídeo")

#Coleta dados do browser
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('window-size=800x600')
options.add_argument('--headless')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#acessando dados
try:
	driver.get(arg)
	site = arg
	time.sleep(3)
	#nome = driver.find_element(By.XPATH,'//*[@id="title"]/h1/yt-formatted-string/text()').text
	nome = driver.title
	print (nome)
except:
	finalizar()
	print("Não foi possível encontrar o vídeo, confira o link fornecido.")
	os._exit()

finalizar()

#Definindo hora
print("Coletando hora")
now = datetime.now()
hora = now.strftime(" %d.%m.%Y - %H.%M")

#Remove caracteres do nome do arquivo.
caracterers = '[!@:|]\/'
for char in caracterers:
		nome = nome.replace(char, "")

#Montando comando de coleta
gravador = 'streamlink --hls-live-restart --retry-streams 2 -o "'+nome+hora+'.mp4" '+arg+' "720p,best"'

#Montando tela do shell
os.system("cls")
print(" ")
print(" ")
print(" ")
print("      Para encerrar a gravação precione Ctrl + C")
print(" ")
print(" ")
print(" ")
print ("Local onde será salvo o vídeo")
os.system("cd")
print(" ")
print(" ")
print("Gravando em  3...2...1...0")
os.system(gravador)

