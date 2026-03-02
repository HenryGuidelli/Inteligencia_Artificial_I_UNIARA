def cadastrar():
    print("Cadastrando...")

def listar():
    print("Listando...")

def sair():
    print("Saindo...")

def menu(opcao):
    opcoes = {
        1: cadastrar,
        2: listar,
        3: sair
    }

    funcao = opcoes.get(opcao)
    if(funcao):
        funcao()
    else:
        print("Opção Inválida")

menu(1)
menu(2)
menu(3)