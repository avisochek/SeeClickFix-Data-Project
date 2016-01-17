#!get_street_lengths
###determines the length of each street
###using osm data.

import pickle
import numpy as np
from lxml import etree
import geopy
from geopy import distance
from get_neighborhood import get_neighborhood

def get_street_lengths(street_names):
    data = etree.parse(open("data/new_haven.xml"))

    ## first, go through the data for each way,
    ## and extract the ids for each node involved.
    print "     getting street nodes..."
    street_nodes={}
    for element in data.iter("way"):
        names = element.findall("./tag[@k='name'].")
        if len(names)>0:
            name=names[0].attrib["v"]
            if name in street_names:
                if not name in street_nodes.keys():
                    street_nodes[name]=[]
                refs=[]
                for node in element.iter('nd'):
                    refs.append(node.attrib['ref'])
                street_nodes[name].append(refs)

    print "     getting street coords..."
    street_coords={}
    ## get street coords...
    ## Search the data for each node to get its coordinates
    for name in street_nodes.keys():
        street_coords[name]=[]
        for i in range(len(street_nodes[name])):
            street_coords[name].append([])
            for j in range(len(street_nodes[name][i])):
                street_coords[name][i].append([])
                node = data.find("./node[@id='"+street_nodes[name][i][j]+"']")
                street_coords[name][i][j]=[node.attrib["lon"],node.attrib["lat"]]


    with open("data/nh_bounds.pkl","r") as f: ## todo: include description and/or code for how to obtain bounds
        nh_bounds = pickle.load(f)

    print "     getting street hoods..."
    ### determine the neighborhood and weather or not a node is in New Haven for each node.
    street_innh={}
    street_hood={}
    for name in street_coords.keys():
        street_innh[name]=[]
        street_hood[name]=[]
        for i in range(len(street_coords[name])):
            lngs=[float(j[0]) for j in street_coords[name][i]]
            lats=[float(j[1]) for j in street_coords[name][i]]
            innhs,hoods=get_neighborhood(lngs,lats)
            street_innh[name].append(innhs)
            street_hood[name].append(hoods)

    print "     getting street lengths..."
    ## finally, we calculate the street length by adding
    ## the length between each pair of consecutive nodes
    ## in each segment, and adding the length of each segment,
    ## only considering those nodes within new haven.
    if len(street_coords)>0:
        street_lengths={}
        street_lengths_by_neighborhood={}
        for name,segments in street_coords.items():
            # todo: possible conditional here to eliminate street lengths of 0
            street_lengths[name]=0
            street_lengths_by_neighborhood[name]={}
            for i in range(len(segments)):
                if len(segments[i])>1:
                    for j in range(1,len(segments[i])):
                        distance_between_nodes=geopy.distance.vincenty(tuple(street_coords[name][i][j]), tuple(street_coords[name][i][j-1])).miles
                        ### find the length of the street strictly within new haven...
                        current_node_innh=street_innh[name][i][j]
                        last_node_innh=street_innh[name][i][j-1]
                        if current_node_innh or last_node_innh:
                            if current_node_innh and last_node_innh:
                                street_lengths[name]+=distance_between_nodes
                            else:
                                street_lengths[name]+=distance_between_nodes/2.
                        ### find the length of the street within each neighborhood...
                        current_node_hood=street_hood[name][i][j]
                        last_node_hood=street_hood[name][i][j-1]
                        if not (current_node_hood=="" and last_node_hood==""):
                            if current_node_hood=="":
                                if not last_node_hood in street_lengths_by_neighborhood[name].keys():
                                    street_lengths_by_neighborhood[name][last_node_hood]=distance_between_nodes/2.
                                else:
                                    street_lengths_by_neighborhood[name][last_node_hood]+=distance_between_nodes/2.
                            elif last_node_hood=="":
                                if not current_node_hood in street_lengths_by_neighborhood[name].keys():
                                    street_lengths_by_neighborhood[name][current_node_hood]=distance_between_nodes/2.
                                else:
                                    street_lengths_by_neighborhood[name][current_node_hood]+=distance_between_nodes/2.
                            elif current_node_hood==last_node_hood:
                                if not current_node_hood in street_lengths_by_neighborhood[name].keys():
                                    street_lengths_by_neighborhood[name][current_node_hood]=distance_between_nodes
                                else:
                                    street_lengths_by_neighborhood[name][current_node_hood]+=distance_between_nodes
                            else:
                                if not current_node_hood in street_lengths_by_neighborhood[name].keys():
                                    street_lengths_by_neighborhood[name][current_node_hood]=distance_between_nodes/2.
                                else:
                                    street_lengths_by_neighborhood[name][current_node_hood]+=distance_between_nodes/2.
                                if not last_node_hood in street_lengths_by_neighborhood[name].keys():
                                    street_lengths_by_neighborhood[name][last_node_hood]=distance_between_nodes/2.
                                else:
                                    street_lengths_by_neighborhood[name][last_node_hood]+=distance_between_nodes/2.


        return street_lengths.keys(), street_lengths.values(),street_lengths_by_neighborhood.values()
    else:
        return [],[],[]
