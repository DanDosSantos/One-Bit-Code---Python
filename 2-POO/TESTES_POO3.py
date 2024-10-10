class ContaBancaria:
    def __init__(self, conta, agencia):
        self.conta = conta
        self.agencia = agencia

    def __str__(self):
        return f'Conta: {self.conta} / Agência: {self.agencia}'
    

class ContaPessoal(ContaBancaria):
    def __init__(self, conta, agencia, cpf, saldo):
        super().__init__(conta, agencia)
        self.__cpf = cpf
        self.__saldo = saldo
    
    def get_cpf(self):
        return self.__cpf
    
    def get_salario(self):
        return self.__saldo


pessoa1 = ContaPessoal(25478-9, 4525, 84159716889, 2200)
print(pessoa1)
print(pessoa1.get_cpf())
print(pessoa1.get_salario())
