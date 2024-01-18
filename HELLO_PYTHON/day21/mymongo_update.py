import pymongo
 
mycon = pymongo.MongoClient("mongodb://localhost:27017")
mytable = mycon.python.sample 
 
mycondition = {"col01" : "5"}
myset = {"$set": {"col02" : "7","col03" : "7"}}
ret_row = mytable.update_one(mycondition, myset)
print(ret_row)
