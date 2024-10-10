from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista =
fruits = ['Maça', 'Banana', 'Pera', 'Uva', 'Banana', 'Laranja', 'Abacaxi', 'Uva', 'Banana', 'Melancia', 'Uva', 'Banana', 'Maça', 'Jabuticaba']
print(Counter(fruits))


# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('Ea FC 24', 100, 7.5)
g2 = game('Fortnite', 'Free', 9.0)
print(g1)
print(g2)


# 3 - Ordenando dicionários
studants = {"Pedro":23, "Ana":22, "Ronaldo":30, "Janaina":25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)


# 4 - Utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)    # add no início
print(deq)
deq.append(90)    # add no fim
deq.popleft()    # remover do inicio
deq.pop()      # remover do fim
print(deq)