#program to split a json file exported from mongodb (with mongoexport)
import json
import os

mydata= ['users.json', 'network.json']
path1 = os.path.join('/home/ubuntu/lastfm/data',mydata[0])

data_1 = []

def m1(myfile):
    """
    strips each line in the json file and append it into the list data_1.
    returns the type of the list's first elements
    """
    
    data_json = open(myfile)
    
    for line in data_json:
        data_1.append(line.strip())
    
    return data_1[0:5]


data_2 = []
range0 = [range(500000), range(500000, 1000000),
         range(1000000, 1500000), range(1500000, 2000000),
         range(2000000, 2500000), range(2500000, 3000000),
         range(3000000, 3500000), range(3500000, 4000000),
         range(4000000, 4500000), range(4500000, 4630838)]

def m2(mylist):
    """
    take each element of mylist and load it as json.
    returns a list of json files.
    """
    
    for item in range0:
        for r in item:
            string = json.loads(mylist[r])
            data_2.append(string)
    
    return data_2[0:10]

#def subset():
#    for item in data_3:
#        if item['country']=='US':
#            data.append(item)
    
#    return type(data[0])
    