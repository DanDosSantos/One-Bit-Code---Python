# Trazer os cursos em ordem alfabética
cursos = []

with open('3-Arquivos/cursos.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linguagem, categoria = linha.rstrip().split(',')
        cursos.append(f'{linguagem} - {categoria}')

for curso in sorted(cursos):
    print(curso)