import pymongo
client = pymongo.MongoClient("mongodb+srv://shubham:shubham1250@shubham.nuxwv7x.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" : "shubham",
    "email" : "yadav.10shubham@gmail.com",
    "surname" : "yadav"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)