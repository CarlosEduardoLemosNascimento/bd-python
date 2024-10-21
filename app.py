import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BANCO_ALUNO = create_engine("sqlite:///banco_aluno.db")

# Criando conexão com banco de dados
Session = sessionmaker(bind=BANCO_ALUNO)
session = Session()

# Criando tabela
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    # Definindo campos da tabela
    ra = Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# Função para criar a tabela
def criar_tabela():
    Base.metadata.create_all(bind=BANCO_ALUNO)

# Função para inserir um aluno
def inserir_aluno(nome, sobrenome, email, senha):
    os.system("cls || clear")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    aluno = Aluno(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
    session.add(aluno)
    session.commit()
    print(f"Aluno {nome} {sobrenome} inserido com sucesso!")

# Função para exibir todos os alunos
def exibir_alunos():
    print("\nExibindo dados de todos os alunos:")
    lista_alunos = session.query(Aluno).all()
    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.nome} {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# Função para atualizar os dados de um aluno
def atualizar_aluno(email_atual):
    aluno = session.query(Aluno).filter_by(email=email_atual).first()
    if aluno:
        aluno.nome = input("Digite o novo nome: ")
        aluno.sobrenome = input("Digite o novo sobrenome: ")
        aluno.email = input("Digite o novo email: ")
        aluno.senha = input("Digite a nova senha: ")
        session.commit()
        print(f"Aluno {aluno.nome} atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

# Função para excluir um aluno
def excluir_aluno(email_excluir):
    aluno = session.query(Aluno).filter_by(email=email_excluir).first()
    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} excluído com sucesso!")
    else:
        print("Aluno não encontrado.")

# Função para consultar um único aluno pelo email
def consultar_aluno(email_consultar):
    aluno = session.query(Aluno).filter_by(email=email_consultar).first()
    if aluno:
        print(f"RA: {aluno.ra}, Nome: {aluno.nome} {aluno.sobrenome}, Email: {aluno.email}")
    else:
        print("Aluno não encontrado.")

# Função principal
def main():
    os.system("cls || clear")
    criar_tabela()

    while True:
        print("\n1 - Inserir Aluno")
        print("2 - Exibir Todos os Alunos")
        print("3 - Atualizar Aluno")
        print("4 - Excluir Aluno")
        print("5 - Consultar Aluno")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            sobrenome = input("Digite o sobrenome do aluno: ")
            email = input("Digite o email do aluno: ")
            senha = input("Digite a senha do aluno: ")
            inserir_aluno(nome, sobrenome, email, senha)

        elif opcao == "2":
            exibir_alunos()

        elif opcao == "3":
            email_atual = input("Digite o email do aluno a ser atualizado: ")
            atualizar_aluno(email_atual)

        elif opcao == "4":
            email_excluir = input("Digite o email do aluno a ser excluído: ")
            excluir_aluno(email_excluir)

        elif opcao == "5":
            email_consultar = input("Digite o email do aluno a ser consultado: ")
            consultar_aluno(email_consultar)

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executando o programa principal
if __name__ == "__main__":
    main()
