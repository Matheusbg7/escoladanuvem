"""
Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

- Distância percorrida: 300 km
- Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Calculadora de consumo de cobustivel

# Dados da viagem
distancia_percorrida = 300 # em quilometros
combustivel_gasto = 25 # em litros (1)

# Calculo do consumo médio 
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("Dados da viagem")
print(f"Distancia percorrida: {distancia_percorrida}(km)") 
print(f"Combustivel gasto: {combustivel_gasto} litros(1)")
print("Consumo médio", round(consumo_medio, 2), "km/1")

#print(consumo_medio)

