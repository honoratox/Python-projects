from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey #sqlalchemy permite que você use a sintaxe python pra fazer as operações no banco de dados
from sqlalchemy.orm import sessionmaker, declarative_base #o session é pra criar a sessão e o declarative base é pra criar as tabelas do banco de dados

db = create_engine("sqlite:///C:/Users/phhonorato/Downloads/webPython/Python&SQLAlchemy/banco.db") #conexão com o banco de dados local

#criar a sessão
Session = sessionmaker(bind=db) #cria o objeto da sessão com o nome do banco de dados
session = Session() #cria efetivamente a sessão chamando o objeto (Session)


#crias tabelas
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios" #essencial ter um tablename em todas as tabelas que forem criadas

    id = Column("id", Integer, primary_key=True, autoincrement=True) #deve ser passado o nome do campo (id) e o tipo de informação que pode receber (Interger), so pode receber numeros
                                                                     #primary_key = define um valor único que identifica aquele item específico no banco
                                                                     #autoincrement = sempre um novo usuário vai ser um id acima do anterior
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True): #o usuário ja vai ser criado ativo
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo       

class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qntd_paginas = Column("qntd_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id")) #nesse caso o 'dono' ta associado ao objeto usuário, uma vez que um usuário pode ter vários livros, pra isso usamos a ForeignKey
    
    def __init__(self, titulo, qntd_paginas, dono):
        self.titulo = titulo
        self.qntd_paginas = qntd_paginas
        self.dono = dono

Base.metadata.create_all(bind=db) #cria todas as tabelas criadas no 'Base' no bando de dados em si


#CRUD - Create, Read, Update, Delete

#Create
#usuario = Usuario(nome="Pedro", email="qlqcoisa@gmail.com", senha="123123") #passa os parametros
#session.add(usuario) #adicionar na sessão do banco de dados
#session.commit() #salva a sessão no banco de dados

#Read
#lista_usuarios = session.query (Usuario).all()
#usuario_pedro = session.query(Usuario).filter_by(email="qlqcoisa@gmail.com").first() #filtrar pesquisa por item específico, como email
#print(usuario_pedro)
#print(usuario_pedro.nome)
#print(usuario_pedro.email)

#livro = Livro(titulo="Harry Potter", qntd_paginas="300", dono=usuario_pedro.id) #pra relacionar um livro a um usuário passamos o 'nome' e seu 'id'(que é único)
#session.add(livro)
#session.commit()
#print("Um livro foi associado ao usuario")

#Update
#usuario_pedro.nome = "Pedro Honorato"
#print("Dados Atualizados com sucesso!")
#session.add(usuario_pedro)
#session.commit()

#Delete
#item_delete = session.query(Usuario).filter_by(id=2).first() #passa os parametros para o item a ser deletado
#print("Usuário deletado com sucesso!")
#session.delete(item_delete)
#session.commit()
