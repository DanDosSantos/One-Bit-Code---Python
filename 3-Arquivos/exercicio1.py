'''
Lendo n linhas de um arquivo
- Escreva um programa para ler as primeiras n linhas de um arquivo
1 - O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.
'''

def file(nome, nlinhas):
    from itertools import islice # ---> qtd de linhas
    with open(nome, encoding='utf-8') as arquivo:
        for linha in islice(arquivo, nlinhas):
            print(linha)

file('3-Arquivos/texto.txt', 2)