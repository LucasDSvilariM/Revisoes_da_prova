opcao = 1
numb = int(input("Digite um número: "))

while opcao != 2:

    if numb % 2 == 0 and numb >= 0:
        print("Número par positivo")

    if numb % 2 == 0 and numb < 0:
        print("Número par negativo")

    if numb % 2 != 0 and numb > 0:
        print("Número ímpar positivo")

    if numb % 2 != 0 and numb < 0:
        print("Número ímpar negativo")

    opcao = int(input("Deseja verificar outro número? \n"
                      "Aperte 1 para continuar \n"
                      "ou 2 para encerrar: "))