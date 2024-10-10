# 1 - Listar valores de 0 a 10 que seja menor que 4
listNumbers = [number for number in range(10) if number < 4]
print(listNumbers)

# Forma que usa mais linhas de código
lista = []
for num in range(10):
    lista.append(num)
    if num == 3:
        break
print(lista)

# 2 - Jogos que possuam a letra a
gamesList = ['Mario Odyssey', 'Dk Country',
            'Luigs Mansion', 'Kirby']

newList = [game for game in gamesList if 'a' in game]
print(newList)

# Outra maneira
jogos_a = []
for game in gamesList:
    if 'a' in game:
        jogos_a.append(game)
print(jogos_a)


# 3 - Jogos que zerei
gamesFinished = [game for game in gamesList if game != 'Kirby']
print(gamesFinished)

# Outra maneira
nao_kirby = []
for game in gamesList:
    if game != 'Kirby':
        nao_kirby.append(game)
print(nao_kirby)