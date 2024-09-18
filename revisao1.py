a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

soma = a + b

if soma > c:
    print(f"Resultado da soma {soma} é maior que o valor de C")

elif soma == c:
    print(f"Resultado da soma {soma} é igual ao valor de C")

else:
    print(f"Resultado da soma {soma} é menor que o valor de C")