import pymongo
client = pymongo.MongoClient("mongodb+srv://shubham:shubham1250@shubham.nuxwv7x.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
database = client['inventory']
collection = database['table']
#collection.insert_many(data)
#d = collection.find()
#d = collection.find({"status" : 'A'})                               #filter where status is A
#d = collection.find({"status" : {'$in':['A','P']}})                        #filter where status = A or P
#d = collection.find({"status" : {"$gt":'C'}})                                 #filter where status is greater than C
#d = collection.find({"qty" : {"$gte":75}})                                     #filter where qty is greater or equal to 75
#d = collection.find({"item":'sketch pad' , 'qty' : 95 })                          #filter where item is sketch pad and qty is 95
#d = collection.find({"item":'sketch pad' , 'qty' : {'$gte':75}})                    #filter where item is sketch pad and qty is greater or equal to 75
#d = collection.find({'$or' : [{"item":'sketch pad'} , {'qty' : {'$gte':75}}]})     #filter using or where item is sketch pad or qty is greater or equal to 75
#collection.update_one({'item':'canvas'} , {'$set':{'item':'shubham'}})               #updating operation
#collection.delete_one({'item':'shubham'})                                             #delete operation
d = collection.find({'item':'shubham'})
for i in d:
    print(i)

