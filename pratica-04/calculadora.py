def calculadora():
    while True:
        try:
            num1 = input("Digite o primeiro número: ")
            num1 = float(num1)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")
            continue

        try:
            num2 = input("Digite o segundo número: ")
            num2 = float(num2)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")
            continue

        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida! Por favor, escolha uma operação válida.")
            continue

        if operacao == '/' and num2 == 0:
            print("Erro: divisão por zero não é permitida.")
            continue

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        break

calculadora()