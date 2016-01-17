import pymongo
from pymongo import MongoClient
import urllib2
import json
import numpy as np

client = MongoClient()
db= client.nh_data

ids=[issue["id"] for issue in db.issues.find()]
ids = ids[int(round(.22*len(ids))):]

print len(ids)
i=0.
for id_ in ids:
	i+=1.
	print i/len(ids)
	url = "http://seeclickfix.com/api/v2/issues/"+str(id_)
	response=urllib2.urlopen(url)
	repid = json.loads(response.read())["reporter"]["id"]
	db.issues.update_one({"id":id_},{"$set":{"repid":repid}})
