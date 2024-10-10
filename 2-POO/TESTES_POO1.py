# Alguns exercícios criados da minha cabeça para colocar em prática meu aprendizado até agora sobre POO usando Herança e Polimorfismo
class Times:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def __str__(self):
        return f'Nome do time: {self.nome} \nPaís: {self.pais}'

# Herança
class Futebol(Times):
    def __init__(self, nome, pais, liga):
        super().__init__(nome, pais)
        self.liga = liga

    def exibir(self):
        print(f'Localizado no(a) {self.pais}, o {self.nome} é um time de futebol que disputa o(a) {self.liga} do país.\n')

# Herança com polimorfismo
class Basquete(Times):
    def __init__(self, nome, pais, liga, titulos):
        super().__init__(nome, pais)
        self.liga = liga
        self.titulos = titulos

    def exibir(self):
        print(f'O {self.nome} é um time de basquete localizado nos {self.pais} que disputa a {self.liga} e possui {self.titulos} títulos.\n')

time1 = Futebol('Palmeiras', 'Brasil', 'Brasileirão Série A')
print(time1)
time1.exibir()

time2 = Basquete('Golden State Warriors', 'EUA', 'NBA', 7)
print(time2)
time2.exibir()

