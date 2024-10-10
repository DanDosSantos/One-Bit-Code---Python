from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = { "category": "Fundamentos" }

x = mycol.delete_many(myquery)

print(f"{x.deleted_count} documento excluído")