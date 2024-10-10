# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, considerando descontos de impostos e benefícios.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def descontos(self):
        self.vt = 60
        self.vr = 40
        self.convenio = 70

    def salario_liquido(self):
        self.descontos()  # Calcula os descontos antes de calcular o salário líquido
        descontos = self.vt + self.vr + self.convenio
        salario = self.salario - descontos
        print(F'O salário líquido é R${salario}')

func = Funcionario('André', 2000, 'Assistente')
func.salario_liquido()


# self.descontos() é chamado dentro do método salario_liquido. Isso garante que sempre que salario_liquido for chamado, os descontos serão recalculados e inicializados, evitando qualquer erro relacionado a variáveis não inicializadas.