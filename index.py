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
from selenium.webdriver.common.action_chains import ActionChains

tentativa = str(4)

sites = []
with open("input.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        sites.append(row)

print(sites)


#TODO
# - alimentar variavel sites importando csv
# - passar o número de tentativa via terminal
# - salvar em pastas de acordo com cliente - campanha
# - adicionar suporte pra multiplas classes (acoes[3])

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

# sites = [['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Rádio Jota FM','https://www.radiojotafm.com.br/sidrolandia/','CLICK,class,btFecha'],['Prefeitura de Três Lagoas','Respeito e Empatia','Site e Folha Integração','http://www.folhaintegracao.com/','SCROLL,3'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News','https://www.perfilnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Interno','https://www.perfilnews.com.br/noticias/saude/','CLICK,id,td-image-wrap'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/','SCROLL,2'],['Prefeitura de Três Lagoas','Respeito e Empatia','FM TL News','http://www.fmtlnews.com.br/','ESC']]
# sites = [['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Diário do MS','http://www.diariodoms.com/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Região News','http://www.regiaonews.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Rádio Jota FM','https://www.radiojotafm.com.br/sidrolandia/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Noticidade','https://www.noticidade.com/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','MS Negócios Classificados','http://www.msnegocios.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Sidrolândia News','https://www.sidrolandianews.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','TV Planalto','https://tvplanalto.com/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Visão Popular','https://www.visaopopular.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Rádio Jota FM','https://www.radiojotafm.com.br/sidrolandia/','CLICK,class,btFecha'],['Prefeitura de Três Lagoas','Respeito e Empatia','Site e Folha Integração','http://www.folhaintegracao.com/','SCROLL,3'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News','https://www.perfilnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Interno','https://www.perfilnews.com.br/noticias/saude/','CLICK,id,td-image-wrap'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/','SCROLL,2'],['Prefeitura de Três Lagoas','Respeito e Empatia','FM TL News','http://www.fmtlnews.com.br/','ESC'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Bolsão em Destaque','https://bolsaoemdestaque.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Bolsão em Destaque - Interno','https://bolsaoemdestaque.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Campo Grande News','https://www.campograndenews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Boca do Povo News','https://bocadopovonews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Blog Manoel Afonso','http://manoelafonso.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Jornal Correio MS','https://www.jornalcorreioms.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Midiamax','https://www.midiamax.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Arapuã News','https://arapuanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Arapuã News - Interno','https://arapuanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Arapuã News - Política Interno','https://arapuanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Minuto MS','http://www.minutoms.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','O Marvado','https://omarvado.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Web Favorita FM','https://webfavoritafm.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Web Favorita FM - Eventos','https://webfavoritafm.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Web Favorita FM - Rodapé','https://webfavoritafm.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Três Lagoas no Ar','https://www.treslagoasnoar.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Tribaladas','https://www.tribaladas.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Sem Limites News','https://semlimitesnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Sem Limites News - Interno','https://semlimitesnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Sem Limites News - Vertical','https://semlimitesnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Pantanal Agora','http://www.pantanalagora.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Pantanal Agora - Interno','http://www.pantanalagora.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Imperium Noticias','https://imperiumnoticias.com.br',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Fatos Regionais','http://www.fatosregionais.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Tribuna News','https://www.atribunanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Tribuna MS','https://www.tribunams.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Local News MS','https://www.localnewsms.com',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Atualiza MS','http://www.atualizams.com.br',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Atualiza MS - Interno','http://www.atualizams.com.br',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Top Mídia News','https://www.topmidianews.com.br/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Top Mídia News - Interna','https://www.topmidianews.com.br/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','O Jacaré','https://www.ojacare.com.br/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Diário Patriota','https://diariopatriota.com.br/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Portal na íntegra','https://portalnaintegra.com/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Sul Matogrossense','http://www.osulmatogrossense.com.br/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Primeira Notícia','http://primeiranoticia.com.br/',''],['Fundo Municipal de Saúde','Campo Grande tem escolha','Seven News','http://sevennews.com.br/','']]
#importar bibliotecas 
data = date.today().strftime('%d-%m-%Y')
#cliente = "cliente"


#cria arquivo de erro 
f= open("error"+data+".txt","w+")
font = ImageFont.truetype("./OpenSans-Regular.ttf", size=20)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
for site in sites:
    try:
        driver.get(site[7])
        print(site)
        cliente = site[1]  	
        campanha = site[2]
        site_nome = site[3]	

        path = site[0] + ' - Monitoramento - ' + campanha + ' - ' + site_nome
        #nomeia arquivos
        nome = path + '/' + cliente+'_'+campanha+'_'+site_nome+'_'+data+'_'+tentativa+'.png' 
        full = path + '/' + cliente+'_'+campanha+'_'+site_nome+'_'+data+'full'+tentativa+'.png'
        printoptions = path + '/' + cliente+'_'+campanha+'_'+site_nome+'_'+data+'v'+tentativa+'.png'
        fulloptions = path + '/' + cliente+'_'+campanha+'_'+site_nome+'_'+data+'fullv'+tentativa+'.png'
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

        if(site[10] != ''):
            acoes = site[4].split()
            if(site[10] == 'ESC'):
                #ActionChains(driver).send_keys(keys.ESCAPE).perform()
                try:
                    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
                except:
                    sys.exc_info()[0]
                print('entrou')
                print(f"{bcolors.OKGREEN}ESC FUNCIONOU!!!!!!!!!!!!!!!!!!!!!!!!!!{bcolors.ENDC}")
            elif(acoes[0] == 'SCROLL'):
                scroll = 0
                print('SCROLL')
                while scroll < acoes[1]:
                    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PageDown)
                    print(f"{bcolors.OKGREEN}SCROLL FUNCIONOU!!!!!!!!!!!!!!!!!!!!!!!!!!{bcolors.ENDC}")
                    scroll+=1
                print(acoes[1])
            elif(acoes[0] == 'CLICK'):
                print('CLICK')
                if(acoes[1] == 'íd'):
                    alvo = driver.find_element(By.ID,acoes[2])
                elif(acoes[1] == 'class'):
                    alvo = driver.find_elements(By.CLASS,acoes[2])[0]
                driver.ActionChains(driver).click_and_hold(alvo).perform()
                print(f"{bcolors.OKGREEN}CLICK FUNCIONOU!!!!!!!!!!!!!!!!!!!!!!!!!!{bcolors.ENDC}")
                print(acoes[1])
            driver.set_window_size(1920, 1400)    
            driver.save_screenshot(printoptions)
            im = Image.open(printoptions)
            d = ImageDraw.Draw(im)
            location = (1780, 1300)
            text_color = (0,0,0)
            d.text(location, data, font=font, fill=text_color)
            im.save(printoptions)

            total_height= driver.find_element("xpath", '//body').size["height"]
            driver.set_window_size(1920, total_height)    
            driver.save_screenshot(fulloptions)
    except: 
        print(f"{bcolors.FAIL}FAIL:{bcolors.ENDC} " + site_nome)
        nome_erro = cliente+' '+campanha+' '+site_nome+' '+data
        f.write(nome_erro)
        f.write("\n")
        sys.exc_info()[0]
        f.write("\n")

f.close()
