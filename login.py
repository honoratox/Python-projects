import customtkinter
from tkinter import messagebox #importa a biblioteca de pop-ups
import string #permite usar bibliotecas como is digit e isnumber e etc

#a 'window' é a janela principal da aplicação e o self é pra acessar o atributo atual, ex: self.text = customtkinter.CTkLabel(window, text="Fazer Login") => acesa o lemento text dentro da aplicação de root e fala o que fazer

# Cria a janela principal
window = customtkinter.CTk()

class WindowLogin:
    def __init__(self, window):  # "__init__ é o construtor da classe Windowlogin / 'window' é a janela principal onde os widgets serão colocados
        customtkinter.set_appearance_mode("dark")  # Define a aparência da janela
        customtkinter.set_default_color_theme("blue")  # Define o tema de cores

        window.geometry("500x300")  # Define o tamanho da janela
        self.window = window  # Guarda a referência da janela principal

        self.text = customtkinter.CTkLabel(window, text="Fazer Login")  #cria o elemento Login dentro da janela
        self.email = customtkinter.CTkEntry(window, placeholder_text="Email")  # Campo de entrada para o email / 'placeholder_text' - gere uma orientação do que o usuário tem que preencher (email)
        self.password = customtkinter.CTkEntry(window, placeholder_text="Senha", show="*")  # Campo de entrada para a senha / 'placeholder_text' - gere uma orientação do que o usuário tem que preencher (senha) / 'show' substitui o que digitamos por '*' dentro do campo senha, para que ela não seja mostrada diretamente
        self.loginButton = customtkinter.CTkButton(window, text="Login", command=self.click)  # command = reotrna pra função que informa a ação pra ser realizada no botão
        self.miniCheckbox = customtkinter.CTkCheckBox(window, text="Lembrar Login", command=self.checkBox)  # command = retorna pra função de Caixa de seleção para lembrar login

        # Organiza os widgets na janela pra definir um espaço entre eles
        self.text.pack(padx=10, pady=10)
        self.email.pack(padx=10, pady=10)
        self.password.pack(padx=10, pady=10)
        self.loginButton.pack(padx=10, pady=10)
        self.miniCheckbox.pack(padx=10, pady=10)
    
        self.success_label = None  # Inicialmente sem a label de sucesso

    def click(self):  # Função de chamada ao clicar no botão de login
        email_text = self.email.get()  # 'get' pega o texto do campo de email
        if ('@' not in email_text): #verifica se esse campo tem '@'
            messagebox.showerror("Erro", "Email inválido, tente novamente!")
            return False

        pass_text = self.password.get() # 'get' pega o texto do campo de senha
        if (not (any(char.isupper() for char in pass_text) and 
                 any(char in string.punctuation for char in pass_text) and 
                 any(char.isdigit() for char in pass_text))): #confere se não(not) tem nenhum(any) carac maiusuculo, especial e numero
            messagebox.showerror("Erro!", "Sua senha deve possuir:\n No mínimo 1 caractere maiúsculo\n No mínimo 1 caractere especial\n No mínimo 1 número")
            return False

        # enquanto o return for False, não muda pra proxima página
        # Se todos os testes forem passados, esconda os widgets de login e mostre a mensagem de sucesso
        self.hide_widgets()
        self.show_sucess_message()
        return True

    def hide_widgets(self):
        # Esconde todos os widgets de login
        self.text.pack_forget()
        self.email.pack_forget()
        self.password.pack_forget()
        self.loginButton.pack_forget()
        self.miniCheckbox.pack_forget()

    def show_sucess_message(self):
        # Cria e mostra a mensagem de sucesso
        if self.success_label is None:
            self.success_label = customtkinter.CTkLabel(self.window, text="Login bem-sucedido!", font=("Arial", 24)) # cria um novo label para mostrar a mensagem
            self.success_label.pack(padx=10, pady=20, fill='both', expand=True) #centraliza o texto
        else:
            self.success_label.pack(padx=10, pady=20)

    def checkBox(self):  # Função chamada ao clicar na caixa de seleção
        print("Usuário deseja salvar informações de login")

# Cria a instância da classe WindowLogin e passa a janela principal
app = WindowLogin(window)

# Inicia o loop principal da interface gráfica
window.mainloop()