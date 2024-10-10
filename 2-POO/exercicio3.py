class Viagem:
    def __init__(self, destino):
        self.destino = destino

trip1 = Viagem('São Paulo')
trip2 = Viagem('Rio de Janeiro')
trip3 = Viagem('Bahia')
trip4 = Viagem('Porto Alegre')
trip5 = Viagem('Buenos Aires')
trip6 = Viagem('Montevideu')

print('Olá Viajante! Temos algumas ofertas para você!')
nome = input('Digite o seu nome para começar: ')
print(f'{nome} temos 6 destinos para você.'
      '''
      [1] - São Paulo
      [2] - Rio de Janeiro(Cuidado!)
      [3] - Bahia
      [4] - Porto Alegre
      [5] - Buenos Aires
      [6] - Montevideu
      ''')

escolha = int(input('Selecione o destino da viagem: '))
lista_viagens = [trip1, trip2, trip3, trip4, trip5, trip6]

for opcao in lista_viagens:
    if escolha >= 7:
        print('Esta opção não esta incluida em nossos destinos')
        break
    else:
        print(f'{nome} sua viagem para {lista_viagens[escolha].destino} está marcada!')
        print('Até mais!')
        break