class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} Idade: {self.idade}'

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []
    
    def add_notas(self, *notas):
        self.notas.extend(notas)

    def media(self):
        media = sum(self.notas) / len(self.notas)
        print(f'A media é de {media:.1f}')
        if media <= 4:
            print('Reprovado')
        elif media == 5:
            print('Recuperação')
        else:
            print('Aprovado!')
        

aluno1 = Aluno('Ana', 16, 123)
aluno1.add_notas(8, 7, 7)
aluno1.media()



# nota1 = int(input('Digite a nota: '))
# nota2 = int(input('Digite a nota: '))
# nota3 = int(input('Digite a nota: '))

# media = (nota1 + nota2 + nota3) / 3
# print(media)