par_count = 0
impar_count = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            par_count += 1
        else:
            print(f"{numero} é ímpar.")
            impar_count += 1
    except ValueError:
        print("Erro: entrada inválida. Por favor, insira um número inteiro.")

print(f"\nQuantidade de números pares: {par_count}")
print(f"Quantidade de números ímpares: {impar_count}")