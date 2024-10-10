# Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a velocidade atual.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0

    def velocidade_atual(self):
        print(f'Valocidade do carro: {self.velocidade}km por hora')


carro1 = Carro('Ford', 'Ka')
carro1.acelerar(40)
carro1.frear(10)
carro1.velocidade_atual()