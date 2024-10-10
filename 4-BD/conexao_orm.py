# Estabelendo uma conexao com ORM no POSTGRESQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Dados do meu PostgreSQL
user = 'postgres'
password = 'ds182036'
host = 'localhost'
database = 'blog'

# passar o banco de dados que irá ser utilizado
DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()