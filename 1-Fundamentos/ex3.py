# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.
preco_por_km200 = 0.50
acima_de_200 = 0.35

distancia = int(input('Digite a distancia que vai percorrer: '))
if distancia <= 200:
    preco = distancia * preco_por_km200
else:
    preco = distancia * acima_de_200

print(f'O preço da passagem vai ser R${preco:.2f}')



# Aumento de salário para funcionarios acima de 1.250,00 vai ser de 10% e abaixo disso vai ser de 15%
salario = float(input('Digite o seu salário: '))

if salario > 1250.0:
    novo_salario = (salario * 0.10) + salario
else:
    novo_salario = (salario * 0.15) + salario

print(f'O novo salário vai ser R${novo_salario:.2f}')