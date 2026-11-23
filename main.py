def apresentar_menu():
    print("================================")
    print("       ASTROEXPLORER")
    print("================================")
    print("Bem-vinda ao observatório digital!")
    print()

    print("1 - Sobre o AstroExplorer")
    print("2 - Sair")
    print("3 - Explorar um objeto astronômico")

def mostrar_sobre():
    print("O AstroExplorer é um projeto de exploração astronômica.")


def identificar_objeto(nome):
    return "Objeto selecionado: " + nome

def iniciar():
    apresentar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_sobre()

    elif opcao == "2":
        print("Até a próxima exploração!")

    elif opcao == "3":
        nome = input("Digite o nome do objeto astronômico: ")
        resultado = identificar_objeto(nome)
        print(resultado)

    else:
        print("Opção inválida.")

iniciar()
