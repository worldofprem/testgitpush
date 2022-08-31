
import  pymongo

client = pymongo.MongoClient("mongodb+srv://psprem4459:eZNqHEV_8!s454h@cluster0.qofyebn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "prem",
    "email": "psprem4459@gamil.com",
    "surname": "sharma"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

d = {
    "name": "prem",
    "email": "psprem4459@gamil.com",
    "surname": "sharma"
d = {
    "name": "prem",
    "email": "psprem4459@gamil.com",
    "surname": "sharma"
d = {
    "name": "prem",
    "email": "psprem4459@gamil.com",
    "surname": "sharma"
