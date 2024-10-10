# Para poder ler dados do PostgreSQL para linguagem Python no exemplo 8
import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = 'ds182036',
    host = 'localhost',
    port = '5432'
)