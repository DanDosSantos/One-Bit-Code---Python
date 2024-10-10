import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('banco.db')

cursor = connection.cursor()

class ContaBancaria:
    def __init__(self, conta, cpf):
        self.conta = conta
        self.cpf = cpf
        self.__saldo = 0

    def __str__(self):
        return f'Conta: {self.conta} / CPF: {self.cpf}\n'
    
    def exibir_saldo(self):
        print(f'Seu saldo é de R${self.__saldo:.2f}\n')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente.\n')
        else:
            self.__saldo -= valor
            print('Saque realizado com sucesso!\n')


print('----- Bem vindo ao Banco! -----')
while True:
    try:
        print('O que deseja fazer?')
        print('1. Acessar conta')
        print('2. Consultar saldo')
        print('3. Depositar')
        print('4. Sacar')
        print('5. Sair')

        escolha = int(input('> '))
        
        if escolha == 1:
            conta = int(input('Digite o número da sua conta: '))
            cpf = int(input('Digite seu CPF: '))
            print('-'*50)

            pessoa1 = ContaBancaria(conta, cpf)
            print(pessoa1)
            
        elif escolha == 2:
            pessoa1.exibir_saldo()

        elif escolha == 3:
            entrada = float(input('Qual valor voce deseja depositar? '))
            cursor.execute("""
            INSERT INTO banco (saldo)
            VALUES (?)
            """, (entrada))
            connection.commit()
            print('Depósito realizado com sucesso!\n')
            connection.close()
        
        elif escolha == 4:
            entrada = int(input('Qual o valor de saque? '))
            pessoa1.sacar(entrada)

        elif escolha == 5:
            break
        
        else:
            print('Opção inválida. Escolha uma opção de 1 a 5.')
    except ValueError:
        print('ERRO. Digite apenas números.')