peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso / (altura **2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc: .1f}")
print(f"Classificação: {classificacao}")