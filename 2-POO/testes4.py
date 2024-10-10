class Ave:
    def __init__(self, pena, garra):
        self.pena = pena
        self.garra = garra

    def exibir(self):
        print(f'Cor das penas: {self.pena} \nTipo de garra: {self.garra}')

class Aguia(Ave):
    def __init__(self, pena, garra, velocidade):
        super().__init__(pena, garra)
        self.velocidade = velocidade

    def exibir_aguia(self):
        super().exibir()
        print('Velocidade: ',self.velocidade)

aguia1 = Aguia('Brancas', 'Fortes', 160)
aguia1.exibir_aguia()
