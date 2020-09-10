# -*- coding: utf-8 -*-
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageFont, ImageDraw
from selenium.webdriver.common.action_chains import ActionChains

sites = [['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Diário do MS','http://www.diariodoms.com/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Região News','http://www.regiaonews.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Rádio Jota FM','https://www.radiojotafm.com.br/sidrolandia/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Noticidade','https://www.noticidade.com/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','MS Negócios Classificados','http://www.msnegocios.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Sidrolândia News','https://www.sidrolandianews.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','TV Planalto','https://tvplanalto.com/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Visão Popular','https://www.visaopopular.com.br/',''],['Prefeitura de Sidrolândia','Meu Conselho: Cuide-se','Rádio Jota FM','https://www.radiojotafm.com.br/sidrolandia/','CLICK,class,btFecha'],['Prefeitura de Três Lagoas','Respeito e Empatia','Site e Folha Integração','http://www.folhaintegracao.com/','SCROLL,3'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News','https://www.perfilnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Interno','https://www.perfilnews.com.br/noticias/saude/','CLICK,id,td-image-wrap'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/','SCROLL,2'],['Prefeitura de Três Lagoas','Respeito e Empatia','FM TL News','http://www.fmtlnews.com.br/','ESC'],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Perfil News - Saúde','https://www.perfilnews.com.br/noticias/saude/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Bolsão em Destaque','https://bolsaoemdestaque.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Bolsão em Destaque - Interno','https://bolsaoemdestaque.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Campo Grande News','https://www.campograndenews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Boca do Povo News','https://bocadopovonews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Blog Manoel Afonso','http://manoelafonso.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Jornal Correio MS','https://www.jornalcorreioms.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Midiamax','https://www.midiamax.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Arapuã News','https://arapuanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Arapuã News - Interno','https://arapuanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Arapuã News - Política Interno','https://arapuanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Minuto MS','http://www.minutoms.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','O Marvado','https://omarvado.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Web Favorita FM','https://webfavoritafm.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Web Favorita FM - Eventos','https://webfavoritafm.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Web Favorita FM - Rodapé','https://webfavoritafm.com/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Três Lagoas no Ar','https://www.treslagoasnoar.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Tribaladas','https://www.tribaladas.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Sem Limites News','https://semlimitesnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Sem Limites News - Interno','https://semlimitesnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Sem Limites News - Vertical','https://semlimitesnews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Pantanal Agora','http://www.pantanalagora.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Pantanal Agora - Interno','http://www.pantanalagora.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Imperium Noticias','https://imperiumnoticias.com.br',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Fatos Regionais','http://www.fatosregionais.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Tribuna News','https://www.atribunanews.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Tribuna MS','https://www.tribunams.com.br/',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Local News MS','https://www.localnewsms.com',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Atualiza MS','http://www.atualizams.com.br',''],['Prefeitura de Três Lagoas','Respeito e Empatia','Atualiza MS - Interno','http://www.atualizams.com.br','']]
#importar bibliotecas 
data = date.today().strftime('%d-%m-%Y')
#cliente = "cliente"

#ler sites

#ler datas

#tirar print
f= open("error"+data+".txt","w+")
font = ImageFont.truetype("./OpenSans-Regular.ttf", size=20)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
for site in sites:
    try:
        driver.get(site[3]);
        print(site)
        cliente = site[0]  	
        campanha = site[1]
        site_nome = site[2]	
        #nomeia arquivos
        nome = cliente+'_'+campanha+'_'+site_nome+'_'+data+'1.png' 
        full = cliente+'_'+campanha+'_'+site_nome+'_'+data+'fullv1.png'
        printoptions = cliente+'_'+campanha+'_'+site_nome+'_'+data+'v2.png'
        fulloptions = cliente+'_'+campanha+'_'+site_nome+'_'+data+'fullv2.png'

        time.sleep(3)
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

        if(site[4] != ''):
            acoes = site[4].split()
            if(site[4] == 'ESC'):
                ActionChains(driver).send_keys(keys.ESCAPE).perform()
                driver.set_window_size(1920, 1400)    
                driver.save_screenshot(printoptions)
                im = Image.open(printoptions)
                d = ImageDraw.Draw(im)
                location = (1780, 1300)
                text_color = (0,0,0)
                d.text(location, data, font=font, fill=text_color)
                im.save(printoptions)
                print('ESC')
            elif(acoes[0] == 'SCROLL'):
                print('SCROLL')
                print(acoes[1])
            elif(acoes[0] == 'CLICK'):
                print('CLICK')
                if(acoes[1] == 'íd'):
                    ActionChains(drivers).move_to_element(drivers.find_element_by_id(acoes[2])).click().perform()
                elif(acoes[1] == 'class'):
                    ActionChains(drivers).move_to_element(drivers.find_element_by_class(acoes[2])).click().perform()
                print(acoes[1])
            
                time.sleep(6)
                driver.set_window_size(1920, 1400)    
                driver.save_screenshot(printoptions)
                im = Image.open(printoptions)
                d = ImageDraw.Draw(im)
                location = (1780, 1300)
                text_color = (0,0,0)
                d.text(location, data, font=font, fill=text_color)
                im.save(printoptions)
            
        #driver.find_element_by_id('username').send_keys('admin');
        #driver.find_element_by_id('password').send_keys('admin');
        #driver.find_element_by_id('login').click();
                
    except: 
        nome_erro = cliente+' '+campanha+' '+site_nome+' '+data
        f.write(nome_erro + "\n")

f.close()
