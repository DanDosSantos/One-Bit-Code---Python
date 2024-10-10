import re

def from_text(string):
    item = re.findall("é \w*", string)
    return item[0][2:]  #Pegar do indice 0(primeiro 'é') do indice 2 em diante

print(from_text('Meu videogame é PS5 e o preço é 3600 reais'))