# -*- coding: utf-8 -*-
from logging import error
import sys #coleta o link
import time #tempo de espera da url
from urllib import request, parse
from warnings import catch_warnings #biblioteca da url
from selenium import webdriver #Coleta o nome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime #define a hora
import os #comando para o shell

def finalizar():
	driver.close()
	driver.quit()
	return None

for arg in sys.argv:
	print(arg)
print ("Coletando o nome do vídeo")

#Coleta dados do browser

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=800x600') # optional
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#acessando dados
try:
	driver.get(arg)
	site = arg
	time.sleep(3)
	nome = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text	
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
