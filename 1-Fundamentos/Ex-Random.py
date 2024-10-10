# Exercício: o usuário precisa digitar um número de 1 a 10, e verificar se acertou o número ou não
import random

fim = False

while not fim:
    print('----O que voce deseja fazer?----')
    print('1. Advinhar o número')
    print('2. Sair')

    opcao = input('> ')
    if opcao == '1':
        try:
            input_user = int(input('Digite um número de 1 a 10: '))
            numero = random.randint(1, 10)
            if input_user <= 10:
                if input_user == numero:
                    print('Voce acertou!')
                    break
                else:
                    print('ERROU!')
            else:
                print('Voce precisa digitar um número de 1 a 10!')
        except ValueError:
            print('ERRO. Digite apenas números!')
    elif opcao == '2':
        fim = True
    else:
        print('Opcão inválida!')