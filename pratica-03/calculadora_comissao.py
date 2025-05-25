nome = input("Informe o nome do funcionario: ")

salario_fixo = float(input("Informe o salário fixo: R$ "))
total_vendas = float(input("Informe o total de vendas: R$ "))

comissao = total_vendas * 0.15

total_receber = salario_fixo + comissao

print(f"O valor total a receber será {total_receber: .2f}")
