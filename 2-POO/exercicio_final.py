class Contatos:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f'Nome: {self.nome} / Telefone: {self.telefone} / E-mail: {self.email}'
    

class ContactBook:
    def __init__(self):
        self.contatos = []
    
    def add_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, contato):
        self.contatos.remove(contato)

    def display_contato(self):
        if not self.contatos:
            print('Lista de contatos está vazia')
        else:
            for contato in self.contatos:
                print(contato)
                print('-'*60)

    def search_contact(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                print(contato)
                return contato
        print('Contato não encontrado')

contato_agenda = ContactBook()

while True:
    print('\n --- Opções Agenda de Contatos ---')
    print('1. Adicionar Contato')
    print('2. Remover Contato')
    print('3. Listar Contatos')
    print('4. Buscar Contato')
    print('5. Sair')

    escolha = input('Escolha a opção > ')

    if escolha == '1':
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')

        contato = Contatos(nome, telefone, email)
        contato_agenda.add_contato(contato)
        print('Contato foi adicionado com sucesso')
    elif escolha == '2':
        nome = input('Informe o nome para remover: ')
        contato = contato_agenda.search_contact(nome)
        if contato:
            contato_agenda.remover_contato(contato)
            print('Contato removido com sucesso')
    elif escolha == '3':
        contato_agenda.display_contato()
    elif escolha == '4':
        nome = input('Informe o nome para buscar o contato: ')
        contato = contato_agenda.search_contact(nome)
    elif escolha == '5':
        break
    else:
        print('Opção inválida. Escolha uma opção de 1 a 5.')