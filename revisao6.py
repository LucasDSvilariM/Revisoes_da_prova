peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

imc = peso / (alt ** 2)
resultado = imc
print(f"{resultado:.2f}")

if imc <= 18.5:
    print("Abaixo do peso")

if imc >= 18.6 and imc <= 24.8:
    print("Peso ideal")

if imc >= 25.0 and imc <= 29.9:
    print("Levemente acima do peso")

if imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau 1")

if imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau 2")

if imc >= 40:
    print("Obesidade grau 3")