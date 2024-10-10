# Ler dados do PostgreSQL para linguagem Python
from postgre_conexao_post import conn

cursor_obj = conn.cursor()

cursor_obj.execute("SELECT * FROM game")

#fetchall é para ler 
resultado = cursor_obj.fetchall()
print(resultado)