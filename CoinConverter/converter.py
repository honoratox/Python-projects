import customtkinter

window = customtkinter.CTk()

taxas ={
    "USD": 5,
    "BRL": 1,
    "EUR": 6,
    "BTC": 7
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
        self.resultLabel = customtkinter.CTkLabel(window, text="")

        self.titulo.pack(padx=10, pady=20)
        self.text1.pack(padx=10, pady=5)
        self.moedaOrigem.pack(padx=10, pady=5)
        self.valor.pack(padx=10, pady=5)
        self.espaco.pack(padx=10, pady=5) #define um espaço entre as moedas de conversão
        self.text2.pack(padx=10, pady=5)
        self.moedaDestino.pack(padx=10)
        self.converterButton.pack(padx=10, pady=10)
        self.resultLabel.pack(padx=10, pady=10)


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
                self.resultLabel.configure(text= f"Conversão: {result:.2f} {opcaoMoedaDestino}") #atualiza o valor da label result e printa o resultado na tela
        except ValueError:
            pass

app = Window(window)

window.mainloop()