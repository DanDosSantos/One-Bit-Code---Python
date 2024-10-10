# Usando CSV e utilizando lambda para trabalhar com ordenação em dicionario, não trazendo o títolo do arquivo
import csv

cursos = []

with open('3-Arquivos/cursos.csv', 'r', encoding='utf-8') as arquivo:
    leitura = csv.DictReader(arquivo)  # ---> Módulo para transformar em dict
    for linha in leitura:
        cursos.append({"Linguagem":linha["Language"], "Categoria":linha["Categoria"]})
    
for curso in sorted(cursos, key=lambda curso: curso['Linguagem']):
    print(f'{curso['Linguagem']} - {curso['Categoria']}')