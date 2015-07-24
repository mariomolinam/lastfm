#program to split a json file exported from mongodb (with mongoexport)
import json
import os

mydata= ['users.json', 'network.json']
path1 = os.path.join('/home/ubuntu/lastfm/data',mydata[0])
path2 = os.path.join('/home/ubuntu/lastfm/data',mydata[1])

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
    
    data_json.close()
    
    return len(data_1)


data_2 = []

def m2(mylist):
    """
    take each element of mylist and select playcount and user_id.
    returns a list of .
    mylist is a list of strings.
    """
    
    for i in mylist:
        n = i.index('"playcount":')
        part = i[n:]
        
        s0 = part.find(':')
        e0 = part.find(',')
        number= part[s0+1:e0]
        
        s1 = part.find(':', e0+1)
        e1 = part.find(',', e0+1)
        user = part[s1+1:e1]
        
        data_2.append([user, number])
    
    
    return data_2[0:10]


data_3 = []

def m3(myfile):
    """
    myfile is a file.
    strips each line in myfile and appends only US users in data_1.
    returns the type of the list's first elements
    """
    
    data_json = open(myfile)
    
    for line in data_json:
        a = line.strip()
        part = a.find('"links":')
        data_3.append(part)
    
    data_json.close()
    
    return len(data_3)  
    
