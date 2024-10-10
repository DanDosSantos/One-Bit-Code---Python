# Atualizando a tabela game com Python no PostgreSQL
from postgre_conexao_post import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE game
    SET name = %s,
    year = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ('F1 24', 2024, 3))
conn.commit()
print('Dados atualizados com sucesso')
conn.close()