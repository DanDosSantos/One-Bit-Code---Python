'''
1 - opção w - write
2 - opção a - append
3 - opção r - read
'''
# Leitura de arquivo
with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(f'{linha.strip()}') # ---> strip vai remover os espaços