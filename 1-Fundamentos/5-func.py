# Funçoes recursivas
def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))
    
numero = int(input('Digite o número para o fatorial: '))
print(f'O fatorial de {numero} é {fatorial(numero)}')