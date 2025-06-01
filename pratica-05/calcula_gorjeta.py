def calcular_gorgeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

"""
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada 

    Parâmetros:
    valor_conta (float): O valor total da cinta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

    Retorna:
    float: O valor da gorjeta calculada
"""
total_conta = float(input("Insira o valor total da conta: R$ "))
porcentagem = float(input("Insira a porcentagem da gorjeta (%): "))

gorjeta = calcular_gorgeta(total_conta, porcentagem)


print(f"\nPara uma conta de R$ {total_conta: .2f} a gorjeta de  {porcentagem}% é {gorjeta: .2f}")

