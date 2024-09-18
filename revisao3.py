a = int(input("Digite o valor: "))
b = int(input("Digite o valor: "))

opcao = 1
while opcao != 2:
    if a == b:
        soma = a + b
        c = soma
        print(f"Valor de C é: {c} ")
    else:
        mult = a * b
        c = mult
        print(f"O valor de C é:{c}")

    opcao = int(input("Digite 1 para continuar \n"
                  "ou 2 para encerrar: "))