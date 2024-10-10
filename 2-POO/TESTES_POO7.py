# Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        if self.quantidade == 0:
            print('Produto indisponível')
        else:
            valor_final = self.preco * self.quantidade
            print(f'O valor total de {self.nome} em estoque é de R${valor_final:.2f}')


prod1 = Produto('Refrigerante', 6, 40)
prod2 = Produto('Leite', 4, 0)
prod1.valor_total()
prod2.valor_total()