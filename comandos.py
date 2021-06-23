# -*- coding: utf-8 -*-
from logging import error
import sys #coleta o link
import time #tempo de espera da url
import urllib.request #trata a url
import re
from urllib import request, parse #biblioteca da url
from selenium import webdriver #Coleta o nome
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
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=800x600') # optional
driver = webdriver.Chrome(options=chrome_options)

#acessando dados
driver.get(arg)
site = arg
time.sleep(3)
nome = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
print (nome)
timer = 0
while (timer != ""):	
	try:
		timer = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[19]/div[2]/span[2]/div[1]').text		
		print (timer)
	except:
		try:
			timer = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[19]/div[2]/span[2]/div[2]').text		
			print (timer)
		except:
			print ("Aula iniciada...")		
			timer = ""
	time.sleep(2)

finalizar()

#Definindo hora
print("Coletando hora")
now = datetime.now()
hora = now.strftime(" %d.%m.%Y - %H.%M")

caracterers = '[!@:|]\/'
for char in caracterers:
		nome = nome.replace(char, "")
#Montando comando de coleta
gravador = 'streamlink --hls-live-edge 99999 --hls-segment-threads 5 -o "'+nome+hora+'.mp4" '+arg+' "720p,best"'

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
