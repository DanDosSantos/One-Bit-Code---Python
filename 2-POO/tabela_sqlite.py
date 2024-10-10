import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('banco.db')

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE banco (
        saldo REAL NOT NULL
        );
""")

print('Tabela criada com sucesso.')
# desconectando...
connection.close()