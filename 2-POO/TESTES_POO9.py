# Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas.

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = 0

    def add_consulta(self, valor):
        self.historico += valor

    def exibir_consultas(self):
        print(f'O paciente possui {self.historico} consultas realizadas')

pac1 = Paciente('Janaina', 34)
pac1.add_consulta(3)
pac1.exibir_consultas()