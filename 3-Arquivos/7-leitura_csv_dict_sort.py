# Trabalhando com ordenação em dicionario
cursos = []

with open('3-Arquivos/cursos.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linguagem, categoria = linha.rstrip().split(',')
        curso = {}
        curso['Linguagem'] = linguagem
        curso['Categoria'] = categoria
        cursos.append(curso)
print(cursos)


def get_linguagem(curso):      # Precisa ser criado uma funçao para ordenar por ela
    return curso['Linguagem']

def get_categoria(curso):      # Precisa ser criado uma funçao para ordenar por ela
    return curso['Categoria']

for curso in sorted(cursos, key=get_categoria):  # Ordenando pela key
    print(f"{curso['Linguagem']} - {curso['Categoria']}")