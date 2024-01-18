import pymongo
 
mycon = pymongo.MongoClient("mongodb://localhost:27017")
mytable = mycon.python.sample 
 
mycondition = {"col01" : "4"}
myset = {"$set": {"col02" : "0","col03" : "0"}}
ret_row = mytable.update_many(mycondition, myset)
print(ret_row)
