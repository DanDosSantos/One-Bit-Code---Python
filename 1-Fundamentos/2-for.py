jogos = ['EA FC 24', 'red dead redemption 2', 'spider-man', 'GTA VI']

# 1 - Iterando valores de uma lista
for jogo in jogos:
    print(jogo)

# 2 - Quando a condição for atendida, o loop para
for jogo in jogos:
    if jogo == 'spider-man':
        break
    print(jogo)

# 3 - Quando a condição for atendida, o loop vai pra próxima
for jogo in jogos:
    if jogo == 'spider-man':
        continue
    print(jogo)

# 4 - Avaliação do jogo
nomeJogo = input('Digite o nome do jogo: ')
avaliacoes = int(input('Digite quantas avaliações deseja fazer no jogo: ')) # Num de ranges

sum = 0
for i in range(avaliacoes): # Para cada range ele ira aprensentar isso abaixo
    nota = float(input('Digite a nota do jogo: '))
    sum += nota
    media = sum / avaliacoes

print(f'A nota media do jogo foi de {media:.1f}')