class Esportes:
    categoria = 'Futebol'
    def __init__(self, time, pais, liga):
        self.time = time
        self.pais = pais
        self.liga = liga

    def info(self):
        print(f'Categoria: {Esportes.categoria}')
        print(f'Nome do time: {self.time} \nPaís: {self.pais} \nLiga que joga: {self.liga}\n')
    
clube = Esportes('Palmeiras', 'Brasil', 'Brasileirão')
clube2 = Esportes('Bayern Munchen', 'Alemanha', 'Bundesliga')
basquete = Esportes('Celtics', 'USA', 'NBA')
basquete2 = Esportes('Real Madrid Basket', 'Espanha', 'Liga ACB')
clube.info()
clube2.info()

# Mudando a categoria de esporte
Esportes.categoria = 'Basquete'  # de futebol para basquete
basquete.info()
basquete2.info()

