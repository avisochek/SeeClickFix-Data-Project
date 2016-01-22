#!scf_data_download
### Download data from the SeeClickFix
### api and return as a group of python
### lists representing the data

import urllib2
import json

def get_data(latest_date):
    ## get request types and ids from api
    request_ids=[]
    request_titles=[]
    request_url="https://seeclickfix.com/api/v2/issues/new?address=New+Haven,+CT"
    response=urllib2.urlopen(request_url)
    request_types=json.loads(response.read())
    for i in request_types["request_types"]:
        if i["organization"]=="New Haven":
            request_ids.append(i["url"].split("/request_types/")[1])
            request_titles.append(i["title"])

    ## generate the base url
    base_url="https://seeclickfix.com/api/v2/issues?"
    if latest_date:
        base_url+="after="+latest_date+"&"
    base_url+="status=open,acknowledged,closed,archived"
    base_url+="&per_page=100&request_types="
    ids,repids,rtids,rtts,times,acks,statuses,addrs,lngs,lats,acknowledged_ats,closed_ats=[],[],[],[],[],[],[],[],[],[],[],[]

    ## iteratively get the data by request type
    ## and then by page number
    for q in range(len(request_ids)):
        print "     getting "+request_titles[q]
        base_url2=base_url+request_ids[q]+"&page="
        page=1
        data=[0]
        while len(data)>0:
            url=base_url2+str(page)
            response=urllib2.urlopen(url)
            data = json.loads(response.read())["issues"]
            for document in data:
                ids.append(document["id"])
		repids.append(document["reporter"]["id"])
                rtids.append(request_ids[q])
                rtts.append(request_titles[q])
                times.append(document["created_at"])
                acks.append(document["acknowledged_at"]!="")
                statuses.append(document["status"])
                addrs.append(document["address"])
                lngs.append(document["lng"])
                lats.append(document["lat"])
		acknowledged_ats.append(document["acknowledged_at"])
		closed_ats.append(document["closed_at"])
            page+=1
    return ids,repids,rtids,rtts,times,acks,statuses,addrs,lngs,lats,acknowledged_ats,closed_ats
