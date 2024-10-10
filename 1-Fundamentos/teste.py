import webbrowser

while True:
    print('-----Escolha uma opção abaixo----')
    print('1 - Entrar no google')
    print('2 - Entrar no twitter')
    print('3 - Entrar no youtube')
    print('4 - Sair')

    opcao = input('> ')
    if opcao == '1':
        webbrowser.open('https://www.google.com.br/')
    elif opcao == '2':
        webbrowser.open('https://www.twitter.com/home')
    elif opcao == '3':
        webbrowser.open('https://www.youtube.com.br/')
    elif opcao == '4':
        break
    else:
        print('ERRO, opção inválida!')