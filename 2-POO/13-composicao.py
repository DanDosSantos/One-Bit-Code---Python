class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Fish(Animal):
    pass

class Parrots(Animal):
    pass

class Zoo:
    def __init__(self):
        self.animals_dict = {} #self_animals.dict é uma variável de dicionario vazia

    def add_animal(self, animal):
        self.animals_dict[animal] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f'No nosso zoológico temos {result} quantidade de {category}'
    
zoo = Zoo()
peixe = Fish('Nemo', 'Mamíferos')
peixe2 = Fish('Dori', 'Mamíferos')
print(vars(peixe))  # Vai printar o que foi passado no argumento PEIXE
papagaio = Parrots('Louro', 'Aves')
print(vars(papagaio))  # Vai printar o que foi passado no argumento PAPAGAIO
zoo.add_animal(peixe)  # Add o objeto a função
zoo.add_animal(peixe2)
zoo.add_animal(papagaio)
print(zoo.total_of_category('Aves'))
print(zoo.total_of_category('Mamíferos'))