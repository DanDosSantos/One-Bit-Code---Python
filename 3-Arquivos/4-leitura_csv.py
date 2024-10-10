# Trabalhando com arquivos CSV

with open('3-Arquivos/cursos.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # row = linha.rstrip().split(',')
        # print(f'{row[0]} - {row[1]}')
        linguagem, categoria = linha.rstrip().split(',')
        print(f'{linguagem} - {categoria}')