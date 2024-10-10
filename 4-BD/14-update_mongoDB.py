# Atualizando informação no MongoDB

from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = { "category": "Fundamentos da Ciencia de dados" }
newvalues = { "$set": { "category": "Fundamentos" } }

mycol.update_one(myquery, newvalues)

# Trazendo todos no Python
for x in mycol.find():
    print(x)