# Acessando os métodos que estão privados e alterando
class Pessoa:
    def __init__(self, nome, idade, cpf, salario):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__salario = salario

    def get_cpf(self):
        return self.__cpf
    
    def get_salary(self):
        return self.__salario
    
    def set_salary(self, salario):
        self.__salario = salario

pessoa1 = Pessoa('Beatriz', 25, 46537891425, 2400)
# print(pessoa1.__cpf)    # Não vai conseguir acessar pois o método é privado
print(pessoa1.nome)
print(pessoa1.get_cpf())
print(pessoa1.get_salary())
pessoa1.__salario = 3500      # Nõ vai conseguir alterar pois o método é privado
pessoa1.set_salary(3000)     # Altera o valor do salário 
print(pessoa1.get_salary())