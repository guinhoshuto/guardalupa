# -*- coding: utf-8 -*-
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageFont, ImageDraw

sites = [['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','MidiaMax','https://www.midiamax.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Campo Grande News','https://www.campograndenews.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Online Midias','http://onlinemidias.com/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Moreninha News','http://moreninhasnews.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Manchete News MS','http://manchetenewsms.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Portal Mídias','https://portalmidias.com'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Bandeira News','https://bandeiranews.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','NoticiandoMS','http://noticiandoms.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','M Midia News','http://www.mmidias.com.br/site/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Notícias CG','https://www.noticiascg.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Da Hora News','http://dahoranews.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Midia CG','https://midiacg.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','CG Morena News','http://cgmorenanews.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Circulando News','http://www.circulandonews.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Interativa News','http://interativanews.com/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Direto das Ruas','https://diretodasruas.com.br/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','GDS News','http://tvgdsnews.com/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','A Voz Indígena','https://www.avozindigena.com.br/site/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','JN Um só corpo','http://jornalumsocorpo.com/'],['Prefeitura Municipal de Campo Grande','Refis 100% Saúde','Blog do Eliezer','https://eliezerdavidvelholobo.blogspot.com/2020/07/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','Diário do MS','http://www.diariodoms.com/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','MS Negócios Classificados','http://www.msnegocios.com.br/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','Noticidade','https://www.noticidade.com/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','Rádio Jota FM','https://www.radiojotafm.com.br/sidrolandia/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','Região News','http://www.regiaonews.com.br/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','Sidrolândia News','https://www.sidrolandianews.com.br/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','TV Planalto','https://tvplanalto.com/'],['Prefeitura de Sidrolândia','Não é hora de relaxar','Visão Popular','https://www.visaopopular.com.br/'],['Prefeitura de Corumbá','IPTU 2020','MS No Ar','https://msnoar.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Diário Corumbaense','https://diarionline.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Cidade Branca','http://www.cidadebranca.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Capital do Pantanal','http://www.capitaldopantanal.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Pérola News','https://perolanews.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Roda Viva MS','https://rodavivams.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Imprensa MS','https://imprensams.com.br/'],['Prefeitura de Corumbá','IPTU 2020','TV Pantaneira','http://www.tvpantaneira.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Correio de Corumbá','https://www.correiodecorumba.com.br/'],['Prefeitura de Corumbá','IPTU 2020','Grupo Pantanal','http://www.grupopantanalms.com.br/principal'],['Prefeitura de Corumbá','IPTU 2020','Grupo Pantanal','http://www.grupopantanalms.com.br/principal'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Campo Grande News','https://www.campograndenews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Site e Folha Integração','http://www.folhaintegracao.com/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Bolsão em Destaque','https://bolsaoemdestaque.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Boca do Povo News','https://bocadopovonews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Blog Manoel Afonso','http://manoelafonso.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Jornal Correio MS','https://www.correiodoms.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Correio de Três Lagoas','http://www.correiodetreslagoas.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Perfil News','https://www.perfilnews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Perfil News','https://www.perfilnews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Perfil News','https://www.perfilnews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Midiamax','https://www.midiamax.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Arapua MS','https://arapuanews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Arapua MS','https://arapuanews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Minuto MS','http://www.minutoms.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Marvado','https://omarvado.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Folha de Três Lagoas','http://www.folhatreslagoas.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Folha de Três Lagoas','http://www.folhatreslagoas.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Dia a Dia','http://jornaldiadia.com.br/2020/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Web Favorita FM','https://webfavoritafm.com/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Web Favorita FM','https://webfavoritafm.com/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Três Lagoas no ar','https://www.treslagoasnoar.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Tribaladas','https://www.tribaladas.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Gospel 3','http://www.gospel3.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Gospel 3','http://www.gospel3.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Sem Limites News','https://semlimitesnews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Sem Limites News','https://semlimitesnews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','FM TL News','http://www.fmtlnews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Pantanal Agora','http://www.pantanalagora.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Fatos Regionais','http://www.fatosregionais.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Tribuna MS','https://www.tribunams.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Entrevista News','http://www.entrevistanews.com.br/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Jornal do Estado MS','https://www.jornaldoestadoms.com/'],['Prefeitura de Três Lagoas','Covid 19 - Orientações','Tribuna News','https://www.atribunanews.com.br/'],['Prefeitura Municipal de Campo Grande','Escolhas','Blog Da Onça','https://aonca.com.br/'],['Prefeitura Municipal de Campo Grande','Escolhas','Campo Grande News','https://www.campograndenews.com.br/'],['Prefeitura Municipal de Campo Grande','Escolhas','Midiamax','https://www.midiamax.com.br/'],['Prefeitura Municipal de Campo Grande','Escolhas','Capital News','https://capitalnews.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','ContraPonto MS','http://www.contrapontoms.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Dourados Agora','https://www.douradosagora.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Folha do MS','http://www.folhadoms.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Estado Notícias','http://www.estadonoticias.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Folha de Dourados','https://www.folhadedourados.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Revista DaGente','https://www.revistadagente.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Jornal Diário MS','https://diarioms.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Douranews','http://www.douranews.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Dourados News','https://www.douradosnews.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','MGS News','http://mgsnews.com.br/portal/'],['Prefeitura de Dourados','Proteja quem você ama','Gazeta do Campo','http://www.gazetadocampo.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','O Vigilante','https://ovigilantems.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Jornal Preliminar','https://www.jornalpreliminar.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','Estado Notícias','http://www.estadonoticias.com.br/'],['Prefeitura de Dourados','Proteja quem você ama','GDS News','http://tvgdsnews.com/'],['Prefeitura de Dourados','Proteja quem você ama','Enfoque MS','https://www.enfoquems.com.br/']]
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
driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options);
for site in sites:
    try:
        driver.get(site[3]);
        print(site)
        cliente = site[0]  	
        campanha = site[1]
        site_nome = site[2]	
        nome = cliente+'_'+campanha+'_'+site_nome+'_'+data+'3.png'
        full = cliente+'_'+campanha+'_'+site_nome+'_'+data+'full.png'
        time.sleep(5)
        driver.set_window_size(1920, 1400)    
        driver.save_screenshot(nome);
        im = Image.open(nome)
        d = ImageDraw.Draw(im)
        location = (1780, 1300)
        text_color = (0,0,0)
        d.text(location, data, font=font, fill=text_color)
        im.save(nome)

        total_height= driver.find_element("xpath", '//body').size["height"]
        driver.set_window_size(1920, total_height)    
            
        #driver.find_element_by_id('username').send_keys('admin');
        #driver.find_element_by_id('password').send_keys('admin');
        #driver.find_element_by_id('login').click();
                
        driver.save_screenshot(full);
        print(nome)
    except: 
        nome_erro = cliente+' '+campanha+' '+site_nome+' '+data
        f.write(nome_erro)

f.close()
