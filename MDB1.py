import pymongo
client = pymongo.MongoClient("mongodb+srv://NiharVaghela:Nihar%401995@niharvaghela.lgh7w.mongodb.net/?retryWrites=true&w=majority&appName=NiharVaghela")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1= client['mongotest']
coll= db1['test']
coll.insert_one(d)
