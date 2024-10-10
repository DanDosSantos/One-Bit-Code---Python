class Animal:
    def __init__(self, especie, tamanho, cor):
        self.especie = especie
        self.tamanho = tamanho
        self.cor = cor
    
    def comer(self):
        print(f'O {self.especie} esta comendo')

class Cavalo(Animal):
    def __init__(self, especie, tamanho, cor, raca):
        super().__init__(especie, tamanho, cor)
        self.raca = raca

    def fugir(self):
        super().comer()
        print(f'O {self.especie} fugiu')

class Leao(Animal):
    def __init__(self, especie, tamanho, cor, juba):
        super().__init__(especie, tamanho, cor)
        self.juba = juba

    def cacar(self):
        print(f'O {self.especie} esta caçando')


cachorro = Animal('Cachorro', 1.20, 'Marrom')
cachorro.comer()
cavalo = Cavalo('Cavalo', 5, 'Preto', 'Corrida')
cavalo.fugir()