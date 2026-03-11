import random

def jogar():
    # Mapeamento das regras: Chave vence os itens da lista
    # O valor da tupla contém (o que ele vence, a ação que realiza)
    regras = {
        "pedra": {"tesoura": "quebra", "lagarto": "esmaga"},
        "papel": {"pedra": "cobre", "spock": "refuta"},
        "tesoura": {"papel": "corta", "lagarto": "decapita"},
        "lagarto": {"spock": "envenena", "papel": "come"},
        "spock": {"tesoura": "esmaga", "pedra": "vaporiza"}
    }

    print("--- Pedra, Papel, Tesoura, Lagarto ou Spock ---")
    escolha_usuario = input("Escolha sua arma: ").lower().strip()

    if escolha_usuario not in regras:
        print("Escolha inválida! Tente novamente.")
        return

    escolha_computador = random.choice(list(regras.keys()))
    print(f"Computador escolheu: {escolha_computador.capitalize()}")

    # Lógica do vencedor
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif escolha_computador in regras[escolha_usuario]:
        acao = regras[escolha_usuario][escolha_computador]
        print(f"Você venceu! {escolha_usuario.capitalize()} {acao} {escolha_computador.capitalize()}.")
    else:
        acao = regras[escolha_computador][escolha_usuario]
        print(f"Você perdeu! {escolha_computador.capitalize()} {acao} {escolha_usuario.capitalize()}.")

if __name__ == "__main__":
    jogar()