# Expressão regular
import re

text = 'Eu preciso conseguir um estágio de programador urgente, pois preciso colocar em prática'

# O r significa que estamos trabalhando com uma string bruta (raw string)
# 1 - Indice inicial e final de palavras

match = re.search(r'estágio de programador',text)
print('Índice inicial', match.start())
print('índice final:', match.end())

# 2 - Buscando o índice que possui o ponto
site = 'https://onebitcode.com'
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase
padrao = '[a-m]'
result = re.findall(padrao, text)
print(text)
print(result)


# 4 - Verificando o início de uma string
rule = r'^A'
frases = ['Quero um estágio', 'Quero jogar EA FC 24', 'Preciso de dinheiro']
for frase in frases:
    if re.match(rule, frase):
        print(f'Corresponde: {frase}')
    else:
        print(f'Não corresponde: {frase}')


rule_end = r'!$'  # O sifrão, indica que está no final da frase
frases_2 = 'o dia está lindo!'
match = re.search(rule_end, frases_2)
if match:
    print('Sim, corresponde')
else:
    print('Não corresponde')