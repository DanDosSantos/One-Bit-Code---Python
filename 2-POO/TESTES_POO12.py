# Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de compras, aplicar descontos e calcular o valor total da compra.

class LojaVirtual:
    pass

class Produtos:
    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor

    def __str__(self):
        return f'Produto: {self.produto} \nValor: R${self.valor:.2f}'

    def desconto(self, valor):
        valor_desconto = (valor / 100) * self.valor
        preco_desconto = self.valor - valor_desconto
        print(f'O valor final do produto {self.produto} é R${preco_desconto:.2f}')

prod1 = Produtos('Manteiga', 7)
print(prod1)
prod1.desconto(20)