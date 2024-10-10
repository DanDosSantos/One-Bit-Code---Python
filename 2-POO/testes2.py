class Produtos:
    def __init__(self, produto, preco, quantidade):
        self.nome = produto
        self.preco = preco
        self.quantidade = quantidade

    @classmethod
    def meu_futuro(cls, string):
        import re
        item = re.findall('um \w*', string)
        nome = item[0][2:]
        preco = item[1][2:]
        quantidade = item[2][2:]
        return cls(nome, int(preco), int(quantidade))
    
produto1 = Produtos.meu_futuro('Meu celular é um Iphone 15 Pro, e ele é um 2500 reais, só vou ter um 1')
print(produto1.__dict__)