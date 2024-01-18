import pymongo
 
mycon = pymongo.MongoClient("mongodb://localhost:27017")
mytable = mycon.python.sample 
 

mydict = [
    { "col01" : "5", "col02" : "5", "col03" : "5"},
    { "col01" : "6", "col02" : "6", "col03" : "6"}
]
objs = mytable.insert_many(mydict)
print(objs)