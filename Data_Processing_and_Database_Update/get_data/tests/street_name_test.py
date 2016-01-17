from get_street_name import get_street_name
from pymongo import MongoClient


client = MongoClient()
db = client.nh4

issues = db.issues.find()

addrs=[]
for i in range(100):
    addrs.append(issues.next()["address"])
    
street_names=get_street_name(addrs)
print street_names