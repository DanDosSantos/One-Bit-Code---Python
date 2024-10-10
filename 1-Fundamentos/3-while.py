# Nesse exemplo de while, não sabemos quantas avaliações vão ser feitas até que digite -1
nomeJogo = input('Digite o nome do jogo: ')
qtdAvaliacoes = 0
totalAvaliacoes = 0
media = 0

while True:
    nota = float(input('Informe a nota do jogo: '))
    if nota != -1:
        totalAvaliacoes += nota
        qtdAvaliacoes += 1
        media = totalAvaliacoes / qtdAvaliacoes
    else:
        break
print(f'Media das avaliações do jogo {nomeJogo} é {media:.1f}')