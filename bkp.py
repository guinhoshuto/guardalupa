# -*- coding: utf-8 -*-
import os
import time
import sys
import csv
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image, ImageFont, ImageDraw

tentativa = str(2)

sites = []
with open("sites.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        sites.append(row)

print(sites)

#TODO
# - passar o número de tentativa via terminal
# - adicionar suporte pra multiplas classes (acoes[3])
#-------------------------------------------------------------
#FIX
# - no windows os arquivos estao vindo com caracteres estranhos, possivelmente precise de um UTF-8 no csv 
# - salvar por número de PI, não por nome de site 
# - no windows tem algum problema de allow não sei o que

#firula
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#importar bibliotecas 
data = date.today().strftime('%d-%m-%Y')
#cliente = "cliente"


#cria arquivo de erro 
f= open("error-sites-"+data+".txt","w+")
font = ImageFont.truetype("./OpenSans-Regular.ttf", size=20)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
for site in sites:
    try:
        driver.get(site[1])
        print(site)
        site_nome = site[0]

        path = 'bkp-sites/' + site_nome
        #nomeia arquivos
        nome = path + '/' + site_nome+'_'+data+'_'+tentativa+'.png' 
        full = path + '/' + site_nome+'_'+data+'full'+tentativa+'.png'
        print(nome)


        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                print ("Successfully created the directory %s " % path)

        time.sleep(5)
        driver.set_window_size(1920, 1400)    
        driver.save_screenshot(nome)
        im = Image.open(nome)
        d = ImageDraw.Draw(im)
        location = (1780, 1300)
        text_color = (0,0,0)
        d.text(location, data, font=font, fill=text_color)
        im.save(nome)

        total_height= driver.find_element("xpath", '//body').size["height"]
        driver.set_window_size(1920, total_height)    

        driver.save_screenshot(full)
        print(nome)

    except: 
        print(f"{bcolors.FAIL}FAIL:{bcolors.ENDC} " + site_nome)
        nome_erro = site_nome+' '+data
        f.write(nome_erro)
        f.write("\n")
        sys.exc_info()[0]
        f.write("\n")

f.close()
