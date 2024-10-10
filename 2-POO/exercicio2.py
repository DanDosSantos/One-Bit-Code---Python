class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'Nome do produto: {self.nome} \nPreço do produto: R${self.preco}'

    def desconto(self, percentual):
        # self.percentual = percentual
        # print(f'Preco com desconto: R${self.preco - (self.preco * percentual):.2f}')
        
        # Outra forma
        valorDesconto = (self.preco/100) * percentual
        precoFinal = self.preco - valorDesconto
        print(f'Preço final com desconto: R${precoFinal:.2f}')


produto = Produto('Iphone 15', 6000)
print(produto)
# produto.desconto(0.10)  # Passar como argumento a % de desconto
produto.desconto(10) # 2 maneira
