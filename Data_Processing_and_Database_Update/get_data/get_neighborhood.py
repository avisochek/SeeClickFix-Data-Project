#!get_neighborhood.py

### for each issure, use shapely to determine
## weather issue is in either neighborhood
### and weather issue is in new haven.

### neighborhood data obtained from
### https://github.com/blackmad/neighborhoods/blob/master/new-haven.geojson

### New Haven bounds obtained from
#todo: include instructions to obtain city boundaries...

import json
import pickle
from shapely.geometry import Polygon as pg
from shapely.geometry import Point

def get_neighborhood(lngs,lats):
    with open("data/new_haven.geojson","r") as f:
        neighborhood_data=json.load(f)
    with open("data/nh_bounds.pkl","r") as f:
        nh_bounds = pickle.load(f)

    hoods=[""]*len(lngs)
    innhs=[False]*len(lngs)
    for i in range(len(neighborhood_data["features"])):
        neighborhood = neighborhood_data["features"][i]
        hood_bounds = neighborhood["geometry"]["coordinates"][0][0]
        name = neighborhood["properties"]['name']
        poly = pg(*[hood_bounds])
        poly2 = pg(*[nh_bounds])
        for i in range(len(lats)):
            if poly.contains(Point((lngs[i],lats[i]))):
                hoods[i]=name
            if poly2.contains(Point((lngs[i],lats[i]))):
                innhs[i]=True
    return innhs, hoods
