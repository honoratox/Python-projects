import customtkinter
import requests

# Cria a janela principal usando customtkinter
window = customtkinter.CTk()

estados = {  #dicionário pra armazenar os estados
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}

class Window:
    def __init__(self, window):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        window.geometry("500x650")
        self.window = window

        # Cria os elementos da interface gráfica
        self.titulo = customtkinter.CTkLabel(window, text="Busque seu CEP", font=('arial', 30))
        self.cep = customtkinter.CTkEntry(window, placeholder_text="Digite seu cep", font=('arial', 15))
        self.button = customtkinter.CTkButton(window, text="Buscar", command=self.click, font=('arial', 15))
        self.end = customtkinter.CTkLabel(window, text="", justify="left", font=('arial', 15)) #alinha os conteúdos no centro a esquerda

        # Adiciona os elementos à janela
        self.titulo.pack(padx=10, pady=10)
        self.cep.pack(padx=10, pady=10, )
        self.button.pack(padx=10, pady=10)
        self.end.pack(padx=10, pady=10)

        self.window.bind('<Return>', self.click) #Vincula a tecla Enter/Return ao método click

    def click(self, event=None):
        # Obtém o CEP digitado pelo usuário
        cep_digitado = self.cep.get()

        # Faz uma requisição à API para buscar informações do CEP
        requisicao = requests.get(f"https://cep.awesomeapi.com.br/json/{cep_digitado}")

        if requisicao.status_code == 200: # Verifica se a requisição foi bem-sucedida
            dados = requisicao.json()

            estadosSigla = dados.get('state')
            estadosNomes = estados.get(estadosSigla) #busca um valor no dicionário, no caso se encontrar a sigla, dentro do dicionario, retorna o nome

            # Extrai os dados desejados do JSON
            endereco = f"Endereço: {dados.get('address')} \nBairro: {dados.get('district')} \nCidade: {dados.get('city')} \nEstado: {estadosNomes}, {estadosSigla}" #'f' porque é uma variável
        else:
            endereco = "CEP não encontrado ou inválido."

        # Atualiza o texto do label com o endereço ou a mensagem de erro
        self.end.configure(text=endereco)

# Cria a instância da classe Window e inicia o loop principal
app = Window(window)
window.mainloop()
