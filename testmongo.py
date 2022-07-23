import pymongo
client = pymongo.MongoClient("mongodb://mahesh:mongodb123@application-shard-00-00.tyvxb.mongodb.net:27017,application-shard-00-01.tyvxb.mongodb.net:27017,application-shard-00-02.tyvxb.mongodb.net:27017/?ssl=true&replicaSet=atlas-ws8bdw-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

dic = {"name" :"Maheswar", "email": "parmarctc1@gmail.com", "surname":"Parmar"}

db1 = client['testmongo']
coll = db1['test']
coll.insert_one(dic)