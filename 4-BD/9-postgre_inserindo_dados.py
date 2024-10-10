# Inserindo dados na tabela game do PostgreSQL utilizando Python
from  postgre_conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('Star Wars Survivor', 2023, 9.0),
    ('Luigis Mansion 3', 2019, 9.2)
]

for game in games:
    cursor_obj.execute("""
        INSERT INTO game(name, year, score)
        VALUES (%s, %s, %s)
                        """, game)

# Commit é para poder editar
conn.commit()
print('Dados inseridos com sucesso!')
conn.close()