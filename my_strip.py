#program to split a json file exported from mongodb (with mongoexport)
import json
import os

mydata= ['users.json', 'network.json']
path1 = os.path.join('/home/ubuntu/lastfm/data',mydata[0])

data_1 = []

def m1(myfile):
    """
    myfile is a file.
    strips each line in myfile and appends only US users in data_1.
    returns the type of the list's first elements
    """
    
    data_json = open(myfile)
    
    for line in data_json:
        a = line.strip()
        if "US" in a:
            data_1.append(a)
    
    return data_1[0:5]


data_2 = []
def m2(mylist):
    """
    take each element of mylist and load it as json.
    mylist is a list.
    returns a list of json files.
    """
    
    for item in mylist:
        jsonfile = json.loads(item)
        data_2.append(jsonfile)
        
        #for r in item:
        #    string = json.loads(mylist[r])
        #    data_2.append(string)
    
    return data_2[0:5]

#def subset():
#    for item in data_3:
#        if item['country']=='US':
#            data.append(item)
    
#    return type(data[0])
    