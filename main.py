import os
import json


def carregar_dados():
    if os.path.exists("dados.json"):
        try:
            with open("dados.json", "r") as arquivo:
                return json.load(arquivo)
        except:
            return []
    return []


def salvar_dados():
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios_cadastrados, arquivo, indent=4)

usuarios_cadastrados = carregar_dados()

def menu():
    print("\n1 - Cadastrar usuário \n2 - Listar usuários \n3 - Buscar usuário \n4 - Atualizar usuário \n5 - Deletar usuário \n0 - Sair")
    
    try:
        opcao = int(input("\nDigite uma opção: "))

        if opcao == 1:
            cadastro_usuario()
        elif opcao == 2:
            listar_usuarios()
        elif opcao == 3:
            buscar_usuario()
        elif opcao == 4:
            atualizar_usuario()
        elif opcao == 5:
            deletar_usuario()
        elif opcao == 0:
            print("Saindo...")
            exit()
        else:
            print("Opção inválida!")

    except ValueError:
        print("Digite apenas números!")


def cadastro_usuario():
    try:
        nome = input("\nNome: ")
        idade = int(input("Idade: "))

        if idade <= 0:
            print("Idade inválida")
            return

        email = input("Email: ")

        usuarios_cadastrados.append({
            "nome": nome,
            "idade": idade,
            "email": email
        })
        salvar_dados()

        print(f"\nUsuário {nome} cadastrado com sucesso!")

    except ValueError:
        print("Idade inválida")


def listar_usuarios():
    if len(usuarios_cadastrados) == 0:
        print("Nenhum usuário cadastrado")
        return

    for i, usuario in enumerate(usuarios_cadastrados, start=1):
        print(f"{i} - {usuario['nome']} | {usuario['idade']} | {usuario['email']}")


def buscar_usuario():
    nome_input = input("Digite o nome: ").lower()

    for usuario in usuarios_cadastrados:
        if nome_input == usuario["nome"].lower():
            print("\nUsuário encontrado:")
            print(f"{usuario['nome']} | {usuario['idade']} | {usuario['email']}")
            return

    print("Usuário não encontrado")


def atualizar_usuario():
    listar_usuarios()

    try:
        opcao = int(input("\nDigite o número do usuário: "))

        if opcao <= 0 or opcao > len(usuarios_cadastrados):
            print("Usuário inválido")
            return

        indice = opcao - 1

        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))

        if idade <= 0:
            print("Idade inválida")
            return

        email = input("Novo email: ")

        usuarios_cadastrados[indice]["nome"] = nome
        usuarios_cadastrados[indice]["idade"] = idade
        usuarios_cadastrados[indice]["email"] = email
        salvar_dados()

        print("\nUsuário atualizado com sucesso!")

    except ValueError:
        print("Digite um número válido")


def deletar_usuario():
    listar_usuarios()

    try:
        opcao = int(input("\nDigite o número do usuário para deletar: "))

        if opcao <= 0 or opcao > len(usuarios_cadastrados):
            print("Usuário inválido")
            return

        indice = opcao - 1

        removido = usuarios_cadastrados.pop(indice)
        salvar_dados()

        print(f"\nUsuário {removido['nome']} removido com sucesso!")

    except ValueError:
        print("Digite um número válido")




while True:
    menu()