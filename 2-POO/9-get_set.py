class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Atributo privado

    def exibir(self):
        print(f'Nome: {self.name} - Salário: R${self.__salary}')

    # Metodo para buscar dados
    def get_salary(self):
        return self.__salary
    
    # Metodo para modificar atributo privado
    def set_salary(self, salary):
        self.__salary = salary

fulano = Employee('Mario antonio', 4000)
fulano.name = 'João Pedro'
fulano.exibir()
fulano.set_salary(10000)  # Alterar o valor do atributo pv 
fulano.exibir()