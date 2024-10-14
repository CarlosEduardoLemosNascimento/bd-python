import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados
Session = sessionmaker (bind=MEU_BANCO)
session = Session()

# Criando tabela

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    # Definindo camps da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__ (self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD
# Create - Insert - Salvar
os.system("cls || clear")
print("Solicitante dados para o usuário. ")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# R - Read - select - Consulta
print("\nExibindo dados de todos os clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# U - Update - UPDATE - Atualizar
print("\nAtualizando dados do usuário. ")
email_cliente = input("Digite o e-mail do ciente que será atualizado: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    cliente.nome = input("Digite o seu nome: ")
    cliente.email = input("Digite o seu e-mail: ")
    cliente.senha = input("Digite sua senha: ")

    session.commit()
else:
    print("Cliente não encontrado. ")

# Read - select - Consulta
print("\nExibindo dados de todos os clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# D - Delete - DELETE - Excluir
print("\nExcluindo dados do usuário. ")
email_cliente = input("Digite o e-mail do ciente que será excluido: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} excluído com sucesso. ")
    
else:
    print("Cliente não encontrado. ")

# Read - select - Consulta
print("\nExibindo dados de todos os clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# Read - select - Consulta
print("\nConsultando os dados de apenas um cliente")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
    email_cliente = input("Digite o e-mail do ciente: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
    else:
        print("Cliente não encontrado.")