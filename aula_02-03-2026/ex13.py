def calculadora(a, b, opr):
    if(opr == "+"):
        return a + b
    elif(opr == "-"):
        return a - b
    elif(opr == "*"):
        return a * b
    elif(opr == "/"):
        return a / b
    else:
        return "Opção inválida!"

print(calculadora(10, 15, "+"))
print(calculadora(10, 15, "-"))
print(calculadora(10, 15, "*"))
print(calculadora(10, 15, "/"))