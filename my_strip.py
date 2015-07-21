#program to split a json file exported from mongodb (with mongoexport)
import json

data_1 = []

def m1(myfile):
    """
    Strips each line in the json file and append it into the list data_1
    """
    data_json = open(myfile)
    
    for line in data_json:
        data_1.append(line.strip())
    
    return type(data_1[0])


data_2 = []
def m2(mylist):
    for item in mylist:
        data_2.append(json.loads(item))

#def subset():
#    for item in data_3:
#        if item['country']=='US':
#            data.append(item)
    
#    return type(data[0])
    