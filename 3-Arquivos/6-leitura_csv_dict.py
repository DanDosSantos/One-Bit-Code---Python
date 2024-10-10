cursos = []

with open('3-Arquivos/cursos.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linguagem, categoria = linha.rstrip().split(',')
        curso = {}
        curso['Linguagem'] = linguagem
        curso['Categoria'] = categoria
        cursos.append(curso)

print(cursos)

for curso in cursos:
    print(f"{curso['Linguagem']} - {curso['Categoria']}")