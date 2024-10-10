# Utilizando lambda para trabalhar com ordenação em dicionario
cursos = []

with open('3-Arquivos/cursos.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linguagem, categoria = linha.rstrip().split(',')
        curso = {}
        curso['Linguagem'] = linguagem
        curso['Categoria'] = categoria
        cursos.append(curso)
print(cursos)

# Ordenando pela key
for curso in sorted(cursos, key=lambda curso: curso['Linguagem']):
    print(f"{curso['Linguagem']} - {curso['Categoria']}")