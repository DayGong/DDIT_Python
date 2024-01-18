import pymongo
 
mycon = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mycon["python"]
mytable = mydb["sample"]
 
for r in mytable.find():
    print(r['col01'],r['col02'],r['col03'])