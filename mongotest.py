import pymongo

client = pymongo.MongoClient("mongodb+srv://maheswar2001:Mahesh@123@pulsar.swl7o.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)