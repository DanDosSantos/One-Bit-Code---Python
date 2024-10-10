# Trazer os nomes em ordem alfabética usando o SORTED
nomes = []

with open('3-Arquivos/nomes.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nomes.append(linha.strip())

for nome in sorted(nomes):
    print(nome)