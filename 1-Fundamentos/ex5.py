# Ex 5 - Escreva uma função que receba uma string e conte o número de letras maiúsculas e minúsculas dessa string.

def my_func(texto):
    tipo = {'Upper': 0, 'Lower': 0}
    for letra in texto:
        if letra.isupper():
            tipo['Upper'] += 1
        elif letra.islower():
            tipo['Lower'] += 1
    print('Texto original:', texto)
    print('Número de letras maiúsculas:', tipo['Upper'])
    print('Número de letras minúsculas:', tipo['Lower'])


my_func('My Egg')


# Ex 5.1 - Lista números pares e ímpares de uma lista, -> Escreva uma função para imprimir os números em duas listas separadas para cada uma.

def par_impar(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

print(par_impar([1, 2, 4, 7, 8, 9, 10, 23, 26]))