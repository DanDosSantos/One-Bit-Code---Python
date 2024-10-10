import webbrowser
# Abrir uma janela no navegador conforme a escolha do usuário

while True:
    print('-----Escolha uma das opções abaixo-----')
    print('1 - Aprender Python')
    print('2 - Aprender sobre módulos')
    print('3 - Aprender Python, Fullstack, JS, Ingles e NoCode')
    print('4 - Sair')

    opcao = input('> ')
    
    if opcao == '1':
        webbrowser.open('https://www.python.org/')
    elif opcao == '2':
        webbrowser.open('https://docs.python.org/pt-br/3.14/')
    elif opcao == '3':
        webbrowser.open('https://pro.onebitcode.com/index.html')
    elif opcao == '4':
        break
    else:
        print('ERRO: Opção inválida, digita um número de 1 a 4')