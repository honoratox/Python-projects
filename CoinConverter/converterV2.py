import customtkinter
import requests
import pandas as pd
from datetime import datetime
import time

class Api:

    def __init__(self):
        self.atualizar_taxas() 
    

    def atualizar_taxas(self):
        #pegar a cotação da moeda
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") #faz uma requisição na API
        requisicao_dic = requisicao.json() #Converte a resposta da API de JSON para um dicionário Python e a armazena na variável requisicao_dic.

        USD = requisicao_dic["USDBRL"]["bid"] #extrai a cotação de compra do Dólar em relação ao Real e a armazena na variável USD.
        EUR = requisicao_dic["EURBRL"]["bid"] #extrai a cotação de compra do Euro em relação ao Real e a armazena na variável EUR.
        BTC = requisicao_dic["BTCBRL"]["bid"] #extrai a cotação de compra do Bitcoin em relação ao Real e a armazena na variável BTC.

        #atualiza as cotações no dicionário 'taxas'
        taxas["USD"] = float(USD)
        taxas["EUR"] = float(EUR)
        taxas["BTC"] = float(BTC)

        #atualiza a cotação na planilha 'Cotações'
        tabela = pd.read_excel("Cotações.xlsx") #informa qual planilha deve ser trabalhada
        tabela.loc[0, "Cotação"] = float(USD) #'tabela.loc' = localiza na tabela a coluna "cotação" e atualiza o valor da cotação do dolar
        tabela.loc[1, "Cotação"] = float(EUR) #'tabela.loc' = localiza na tabela a coluna "cotação" e atualiza o valor da cotação do euro
        tabela.loc[2, "Cotação"] = float(BTC) #'tabela.loc' = localiza na tabela a coluna "cotação" e atualiza o valor da cotação do bitcoin
        tabela.loc[0, "Data Última Atualização"] = datetime.now() #atualiza a coluna data de atualização com a ultima feita

        tabela.to_excel("Cotações.xlsx", index=False) #envia a tabela pro pro arquivo xlsx
        print(f"Cotação atualizada. {datetime.now()}")

taxas ={ #inicializa todas as taxas como 1, porém esses valores são atualizados na função 'atualizar_taxas'
    "USD": 1,
    "BRL": 1,
    "EUR": 1,
    "BTC": 1
}

class Window:
    def __init__(self, window):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        window.geometry("500x650")
        self.window = window

        self.titulo = customtkinter.CTkLabel(window, text = "Conversor de Moedas", font=('arial', 30)) 
        self.text1 = customtkinter.CTkLabel(window, text = "Selecone a moeda de origem:", font=('arial', 18))
        self.text2= customtkinter.CTkLabel(window, text= "Selecione a moeda de destino:", font=('arial', 18))
        self.moedaOrigem = customtkinter.CTkOptionMenu(window, values=["USD", "BRL", "EUR", "BTC"], command=self.click, font=('arial', 18))
        self.moedaDestino = customtkinter.CTkOptionMenu(window, values=["USD", "BRL", "EUR", "BTC"], command=self.click, font=('arial', 18))
        self.valor = customtkinter.CTkEntry(window, placeholder_text= "Digite o valor", font=('arial', 18))
        self.espaco = customtkinter.CTkLabel(window, text="")
        self.converterButton = customtkinter.CTkButton(window, text="Converter", command=self.click, font=('arial', 18))
        self.resultLabel = customtkinter.CTkLabel(window, text="") #result deve ser vazio pois vai atualizar dependendo de qual moeda escolher

        self.titulo.pack(padx=10, pady=20)
        self.text1.pack(padx=10, pady=5)
        self.moedaOrigem.pack(padx=10, pady=5)
        self.valor.pack(padx=10, pady=5)
        self.espaco.pack(padx=10, pady=5) #define um espaço entre as moedas de conversão
        self.text2.pack(padx=10, pady=5)
        self.moedaDestino.pack(padx=10)
        self.converterButton.pack(padx=10, pady=10)
        self.resultLabel.pack(padx=10, pady=10)

        #Cria uma instância de Api e atualiza as taxas
        self.api = Api()

    def click(self):
        opcaoMoedaOrigem = (self.moedaOrigem.get()) #pega qual moeda selecionou
        opcaoMoedaDestino = (self.moedaDestino.get()) #pega qual moeda selecionou
        valorReal = (self.valor.get())

        try:
            valorReal = float(valorReal)
            taxaOrigem = taxas[opcaoMoedaOrigem] #compara qual moeda selecionou e acha seu respectivo valor na lista
            taxaDestino = taxas[opcaoMoedaDestino] #compara qual moeda selecionou e acha seu respectivo valor na lista

            if opcaoMoedaOrigem != opcaoMoedaDestino: #so funciona se as moedas forem diferentes
                resultDiv = taxaOrigem/taxaDestino #verifica quantas vezes a moeda de origem é maior ou menor que a de destino
                result = valorReal*resultDiv
                self.resultLabel.configure(text= f"Conversão: {result:.2f} {opcaoMoedaDestino}") #'configure' atualiza o valor da label result e printa o resultado na tela
        except ValueError:
            pass


window = customtkinter.CTk()
app = Window(window)
window.mainloop()