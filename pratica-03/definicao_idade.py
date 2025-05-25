# Solicita a idade do usuário
idade = int(input("Por favor, informe a sua idade: "))

# Classifica a idade em categorias
if idade < 0:
    print(" Idade invalida!") 
elif idade <= 12:
    print("Voçê e criança")
elif idade <= 17:
    print("Voçê é Adolescente")
elif idade >= 59:
    print("Voçê é Adulto")
else:
    print("Voçê é Idoso")
