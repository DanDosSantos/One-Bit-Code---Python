class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Atributo privado

    def exibir(self):
        print(f'Nome: {self.name} - Salário: R${self.__salary}')


fulano = Employee('Joao Pedro', 4000)
fulano.exibir()
fulano.__salary = 40000  # Não consegue modificar
fulano.exibir()