import pymongo
 
mycon = pymongo.MongoClient("mongodb://localhost:27017")
mytable = mycon.python.sample 
 
mycondition = {"col01" : "4"}
ret_row = mytable.delete_many(mycondition)
print(ret_row)

