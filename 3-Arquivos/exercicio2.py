import os

def add_contato():
    nome = input('Informe o nome: ')
    numero = input('Informe o número de telefone: ')

    contato = f'Nome: {nome} \nNúmero: {numero}'

    with open('3-Arquivos/agenda.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(contato)

def listar_contatos():
    if not os.path.exists('3-Arquivos/agenda.txt'):
        print('Lista de contatos está vazia')
        return
    with open('3-Arquivos/agenda.txt', 'r', encoding='utf-8') as arqivo:
        contatos = arqivo.read()
    print('Lista de Contatos')
    print(contatos)

def deletar_contatos():
    if not os.path.exists('3-Arquivos/agenda.txt'):
        print('Lista de contatos está vazia')
        return
    with open('3-Arquivos/agenda.txt', 'w', encoding='utf-8') as arqivo:
        arqivo.write('')
    print('Contatos excluídos com sucesso!')


while True:
    print('\nAgenda de Contatos')
    print('1. Adicionar Contato')
    print('2. Listar Contatos')
    print('3. Remover Contatos')
    print('4. Sair')

    escolha = input('Escolha a opção (1-4): ')
    if escolha == '1':
        add_contato()
    elif escolha == '2':
        listar_contatos()
    elif escolha == '3':
        deletar_contatos()
    else:
        print('Opção Inválida!')