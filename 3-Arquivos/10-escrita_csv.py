import csv

nome = input('Informe o nome da linguagem que deseja aprender: ')
categoria = input('Qual categoria que a linguagem se encaixa? ')

with open('3-Arquivos/cursos.csv', 'a', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo, lineterminator='\n') # -> ao termino de uma linha \n
    writer.writerow([nome, categoria])  #--> nome e a categoria na mesma linha