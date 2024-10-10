# Lançamento do Foguete
import winsound
contador = 10

while (contador > 0):
        contador -= 1
        print(contador)
winsound.Beep(2500, 500)
print('FOGUETE LANÇADO!')

# Tabuada de um numero
numero = int(input('Tabuada de: '))
inicio = int(input('De: '))
fim = int(input('Até: '))

x = inicio

while x <= fim:
        print(f'Tabuada de {numero} x {x} = {numero * x}')
        x += 1
