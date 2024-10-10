# Removendo dado da tabela game do PostgreSQL usando Python
from postgre_conexao_post import conn

cursor_obj = conn.cursor()

sql = """
     DELETE FROM game
     WHERE id = %s
"""

cursor_obj.execute(sql, (5,))
conn.commit()
print("Dado removido com sucesso")
conn.close()