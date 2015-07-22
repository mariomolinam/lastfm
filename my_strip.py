#program to split a json file exported from mongodb (with mongoexport)
import json

data_1 = []

def m1(myfile):
    """
    strips each line in the json file and append it into the list data_1.
    
    returns the type of the first list's element
    """
    data_json = open(myfile)
    
    for line in data_json:
        data_1.append(json.loads(line))
    
    return data_1[0:5]

data_2 = []
def m2(mylist):
    """
    take each element of mylist and load it as json.
    returns a list of json files.
    """
    for item in mylist:
        data_2.append(json.loads(item))
    
    return data_2[0:10]

#def subset():
#    for item in data_3:
#        if item['country']=='US':
#            data.append(item)
    
#    return type(data[0])
    