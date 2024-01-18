import pymongo
 
mycon = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mycon["python"]
mytable = mydb["sample"]
 

mydict = { "col01" : "4", "col02" : "4", "col03" : "4"}
 
ret_row = mytable.insert_one(mydict)
print(ret_row.inserted_id)