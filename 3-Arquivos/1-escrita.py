nome = input('Digite seu nome: ')
'''
1 - opção w - write
2 - opção a - append
3 - opção r - read
'''
# Alternativa 1
# arquivo = open('nomes.txt', 'a')
# arquivo.write(f'{nome}\n')
# arquivo.close()

# Alternativa 2
with open('nomes.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'{nome}\n')