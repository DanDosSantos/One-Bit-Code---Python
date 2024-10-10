''' Método de classe
1 - O método de classe utiliza o parâmetro referente a classe.
2 - O método de classe pode acessar ou modificar o estado da classe.
3 - Usamos o decorator @classmethod para criar um método de classe.
'''

class Console:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall('é \w*', string) # Pegar a partir do é
        nome = item[0][2:] # O primeiro 'é' vai ser nome
        preco = item[1][2:]  # O segundo 'é' vai ser preco
        return cls(nome, int(preco))
    
ps5 = Console.from_text('Meu videogame é PS5 e o preço é 3600 reais')
wiiu = Console.from_text('Meu videogame é WiiU e o preço é 1500 reais')
print(ps5.__dict__)  # Cria um dicionário
print(wiiu.__dict__)