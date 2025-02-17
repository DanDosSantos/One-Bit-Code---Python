import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("movies.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input("Informe o id do filme que deseja atualizar: "))
name = input("Informe o novo nome do Filme: ")
year = int(input('Informe o ano de lançamento do filme: '))
score = float(input('Informe a nota do filme: '))

# 4 - Atualizando Dados
cursor.execute("""
UPDATE movies set name = ?, year = ?, score = ? 
WHERE id = ?
""", (name, year, score, id))
connection.commit()
print('Dados atualizados com sucesso.')

# 5 - Fechando conexão
connection.close()