# Crie uma classe chamada “Pessoa” que possua atributos para armazenar nome, idade e profissão. Implemente métodos para calcular a idade em anos bissextos e exibir informações da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def calcular_idade_bissextos(self):
        # Considerando que um ano bissexto ocorre a cada 4 anos
        # Aproximadamente 1/4 dos anos são bissextos
        anos_bissextos = self.idade // 4
        return anos_bissextos

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Profissão: {self.profissao}")
        print(f"Anos vividos em anos bissextos: {self.calcular_idade_bissextos()}")

pessoa = Pessoa("João", 30, "Engenheiro")
pessoa.exibir_informacoes()