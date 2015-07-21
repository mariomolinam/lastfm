#program to split a json file exported from mongodb (with mongoexport)
import json

data_1 = []
data_2 = []
data_3 = []
def m(myfile):
    """
    Strips each line in the json file and append it into the list data_1
    """
    data_json = open(myfile)
    
    for line in data_json:
        data_1.append(line.strip())
    
    for item in data_1:
        data_2.append(item.strip())
    
    for item in data_2:
        data_3.append(json.loads(item))
    
    return type(data_3[0])

data = []
def subset():
    for item in data_3:
        if item['country']=='US':
            data.append(item)
    
    return type(data[0])
    