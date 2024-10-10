import statistics

# 1 - Aplicar a média
print(statistics.mean([3, 2, 3, 8, 9]))

# 2 - Aplicar a mediana
# Encontrar o valor central
print(statistics.median([1, 2, 4, 8, 9])) # aqui ira retornar o número do meio
print(statistics.median([1, 2, 3, 7, 8, 9])) # unir os dois do meio e dividir

# 3 - Aplicar a moda
# Número que mais se repete
print(statistics.mode([2, 5, 3, 2, 9, 8, 2, 9]))

