# Antecessor e sucessor de um numero
num = int(input('digite um numero: '))

antecessor = num - 1
sucessor = num + 1

print(f'O antecessor de {num} é {antecessor}, e o sucessor é {sucessor}')


# Media de 4 notas
soma_notas = 0

for nota in range(1,5):
    notas = int(input(f'Digite a nota {nota}: '))
    soma_notas += notas

media = soma_notas / 4
print(f'A media foi de {media}')