import urllib.request
import json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=4769e2641ede462eb3d085b0ee446209'

resposta = urllib.request.urlopen(url)

dados = resposta.read()
dados_json = json.loads(dados)

# print(dados_json['results'])

