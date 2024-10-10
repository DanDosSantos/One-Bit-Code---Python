# *args - Utilizamos ele quando não temos certeza de qts argumentos ter em uma função (nesse caso, qnts numero fazer a soma)

# 1 - Soma de números
def soma(*numeros):
    soma_total = 0
    for numero in numeros:
        soma_total += numero
    print(f'A soma é {soma_total}')

soma(7, 9)         # Exemplo: 7 + 9 =
soma(7, 9, 5, 6)

# **kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento. Os argumentos são passados como um dicionário

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

print('###Curso###')
presentation(name='Python', category='Backend', level='Iniciante')