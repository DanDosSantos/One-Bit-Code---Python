# Inserindo dados no mongoDB

from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

post1 = {
     "title": "Data Science",
     "category": "Fundamentos da Ciencia de dados",
     "author": {
         "name": "Pedro Antonio",
         "email":"pedro@email.com"
    }
}

result = mycol.insert_one(post1)
print('Dados inseridos com sucesso!')