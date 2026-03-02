def validar_senha(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tamanho = len(senha) >= 8

    if(tamanho and tem_maiuscula and tem_numero):
        return "Senha TOP"
    else:
        return "Senha FRACA"



print(validar_senha("123"))
print(validar_senha("senha Forte muito 1234"))