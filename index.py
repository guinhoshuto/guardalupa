import time
from datetime import date
from selenium import webdriver
#importar bibliotecas

#sites = [['OpiniaoNews', 'https://www.opiniaonews.com.br/'], ['OlharMS', 'https://www.olharms.com.br/'], ['DiarioPatriota','https://diariopatriota.com.br/'], ['NoticiasCG','https://www.noticiascg.com.br/'], ['MundoDiario','https://mundodiario.com.br/']] 

sites = [['Prefeitura de Corumbá','Carnaval 2020','Capital do Pantanal','http://www.capitaldopantanal.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Cidade Branca','http://www.cidadebranca.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Correio do Corumbá','https://www.correiodecorumba.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Campo Grande News','https://www.campograndenews.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Capital News','https://capitalnews.com.br/'],['Prefeitura de Dourados','Nota Dourada','ContraPonto MS','http://www.contrapontoms.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Circuito MS','http://www.circuitoms.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Diario Corumbaense','https://diarionline.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Grupo Pantanal','http://www.grupopantanalms.com.br/principal'],['Prefeitura de Corumbá','Carnaval 2020','Grupo Pantanal','http://www.grupopantanalms.com.br/principal'],['Prefeitura de Dourados','IPTU 2020','ContraPonto MS','http://www.contrapontoms.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Digital Notícias','https://digitalnoticias.com.br/'],['Prefeitura de Dourados','IPTU 2020','Dourados News','https://www.douradosnews.com.br/'],['Prefeitura de Dourados','IPTU 2020','DouraNews','http://www.douranews.com.br/'],['Prefeitura de Dourados','IPTU 2020','Enfoque MS','https://www.enfoquems.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Imprensa MS','https://imprensams.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','MS no AR','https://msnoar.com.br/'],['Prefeitura de Dourados','IPTU 2020','Estado Notícias','http://www.estadonoticias.com.br/'],['Prefeitura de Dourados','IPTU 2020','Folha de Dourados','https://www.folhadedourados.com.br/'],['Prefeitura de Dourados','IPTU 2020','Folha do MS','http://www.folhadoms.com.br/'],['Prefeitura de Dourados','Nota Dourada','Estado Notícias','http://www.estadonoticias.com.br/'],['Prefeitura de Dourados','IPTU 2020','Gazeta do Campo','http://www.gazetadocampo.com.br/'],['Prefeitura de Dourados','Nota Dourada','Folha de Dourados','https://www.folhadedourados.com.br/'],['Prefeitura de Dourados','IPTU 2020','GDS News','http://tvgdsnews.com/'],['Prefeitura de Campo Grande','IPTU 2020','Jeferson de Almeida','https://jeffersondealmeida.com.br/'],['Prefeitura de Dourados','Nota Dourada','Gazeta do Campo','http://www.gazetadocampo.com.br/'],['Prefeitura de Dourados','IPTU 2020','Jn Diário MS','https://diarioms.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Jn do Ônibus','https://www.jornaldoonibusms.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','MS no AR','https://msnoar.com.br/'],['Prefeitura de Dourados','IPTU 2020','Jn Preliminar','https://www.jornalpreliminar.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Pérola News','https://perolanews.com.br/'],['Prefeitura de Dourados','IPTU 2020','Jornal MS OnLine','https://jornalmsonline.com.br/'],['Prefeitura de Dourados','Nota Dourada','Jn Diário MS','https://diarioms.com.br/'],['Prefeitura de Dourados','IPTU 2020','Meu MS','https://meums.com.br/'],['Prefeitura de Dourados','IPTU 2020','MGS News','https://mgsnews.com.br/portal/'],['Prefeitura de Dourados','Nota Dourada','Jn Preliminar','https://www.jornalpreliminar.com.br/'],['Prefeitura de Dourados','IPTU 2020','MS Atual','http://msatual.com.br/'],['Prefeitura de Dourados','Nota Dourada','MGS News','https://mgsnews.com.br/portal/'],['Prefeitura de Campo Grande','IPTU 2020','Mundo Diário','https://mundodiario.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Notícia CG News','https://www.noticiascg.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','O Patriota','https://diariopatriota.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Olhar MS','https://www.olharms.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','Portal Sul MS','https://portalsulms.com.br/'],['Prefeitura de Dourados','IPTU 2020','Opinião News','https://www.opiniaonews.com.br/'],['Prefeitura de Dourados','IPTU 2020','Revista DaGente','https://www.revistadagente.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','TV Pantaneira','http://www.tvpantaneira.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Seven News','http://sevennews.com.br/'],['Prefeitura de Corumbá','Carnaval 2020','TV Pantaneira','http://www.tvpantaneira.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Top Mídia News','https://www.topmidianews.com.br/'],['Prefeitura de Campo Grande','IPTU 2020','Voz do MS','http://www.vozdoms.com.br/']]

data = date.today().strftime('%d-%m-%Y')
#cliente = "cliente"

#ler sites

#ler datas

#tirar print
f= open("error"+data+".txt","w+")

driver = webdriver.Chrome(executable_path='./chromedriver');
for site in sites:
    try:
        driver.get(site[3]);
        print(site)
        cliente = site[0]  	
        campanha = site[1]
        site_nome = site[2]	
        nome = cliente+'_'+campanha+'_'+site_nome+'_'+data+'.png'
        time.sleep(2)
        total_height = 100000000
        driver.set_window_size(1920, total_height)    
            
        #driver.find_element_by_id('username').send_keys('admin');
        #driver.find_element_by_id('password').send_keys('admin');
        #driver.find_element_by_id('login').click();
                
        driver.save_screenshot(nome);
        print(nome)
    except: 
        nome_erro = cliente+' '+campanha+' '+site_nome+' '+data
        f.write(nome_erro)

f.close()
