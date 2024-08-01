# ESSE PROJETO ACESSA QUALQUER SITE E FAZ O CADASTRO/INSCRIÇÃO NELE

from selenium import webdriver #selenium é uma biblioteca usada para aplicações web / webdriver trata a conf sempre na versão mais atual do navegador
import time # no meu caso o webdrive tava fechando muito rápido, então vou aumentar manualmente o tempo de execução pra testes


#configuração inicial padrão de todo código com selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install()) #instalar o ChromeDriveManager correspondente ao atual

navegador = webdriver.Chrome(service=servico) #definindo qual vai ser o navegador que vou usar

navegador.get("https://pages.hashtagtreinamentos.com/arquivo-python-1jGh7kZSxQLoznA_GgwnWa8f7LEl3kKCZ?origemurl=hashtag_yt_org_planilhapyt_8AMNaVt0z_M") #com o naveagdor criado, eu passo a url de onde quero acessar

#identificar um elemento da tela e conseguir preencher esse elemento
navegador.find_element('xpath', '//*[@id="section-17877670"]/section/div[2]/div/form/div[1]/div/div/div/input').send_keys("pedrom.honorato@gmail,com") #'find_element' - te permite buscar um elemento especifico no site que vc anexou
                                                                                                                            # 'xpath' - é um item padrão de todo site, mas ele tem uma id que permite a voce buscar por um item especificoo desde que siga um passo a passo pra achar esse id. 1- va no site, 2- f12(inspecionar), 3- selecionar qual parte vc quer automatizar, 4- clicar combotão direito, 5- copy -> copy xpath
                                                                                                                            # 'send_keys' - envia(send) o que vc quer completar(keys) no elemento, nesse caso um email

navegador.find_element('xpath', '//*[@id="section-17877670"]/section/div[2]/div/form/button/span/b').click() # 'click' - fiz o que queria e quero clicar

time.sleep(50) # o valor é em segundos, e deve ser usado após a execução de tudo que voce queira fazer