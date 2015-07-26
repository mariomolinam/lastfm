#program to split a json file exported from mongodb (with mongoexport)
import json
import os

mydata= ['users.json', 'network.json']
path1 = os.path.join('/home/ubuntu/lastfm/data', mydata[0])
path2 = os.path.join('/home/ubuntu/lastfm/data', mydata[1])

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
    takes each element of mylist and select playcount and user_id.
    returns a list of .
    mylist is a list of strings.
    """
    
    for i in mylist:
        n0 = i.index('"playcount":')
        part0 = i[n0:]
        s0 = part0.find(':')
        e0 = part0.find(',')
        number = part0[s0+1:e0]
        
        n1 = i.index('"user_id":')
        part1 = i[n1:]
        s1 = part1.find(':')
        e1 = part1.find('}')
        user = part1[s1+1:e1]
        
        data_2.append([user, number])
    
    
    return data_2[0:10]


data_3 = []

def m3(myfile):
    """
    myfile is a file.
    strips each line in myfile .
    returns the type of the list's first elements
    """
    
    data_json = open(myfile)
    
    for line in data_json:
        a = line.strip()
        #part = a.find('"links":')
        data_3.append(a)#[part:])
    
    data_json.close()
    
    return len(data_3)  

    
data_4 = []

def m4(mylist):
    """
    """
    str1 = ''.join(mylist)
    
    names = []
    for i in range(len(data_2)):
        names.append(data_2[i][0])
    
    for i in names:
        iden = '"user_id":' + names[i]
        user = str1.find(iden)
        n1 = str1.find('}', user)
        
        if n1 > 20000:
            part = str1[user-20000:n1]
        else:
            part = str1[:n1]
        
        n0 = part.rfind('"links":')
        
        data_4.append(str1[n0:n1])
        
    return data_4[0:5]


data_5 = []

def m5(mylist):
    """
    
    mylist is a list of strings.
    """
    
    str1 = ''.join(mylist)
    names = []
    
    for i in range(len(data_2)):
        names.append(data_2[i][0])
    
    track = range(0,700000, 100)
    for i in range(len(names)):
        times = str1.count(names[i])
        num0 = 0
        
        #this is for tracking the process
        #if i in track:
        print i
        
        for k in range(times):
            
            num1 = str1.find(names[i], num0+1)
            num2 = str1.find('}', num1+1)
            if num2 > 10000:
                part = str1[num1-10000:num2]
            else:
                part = str1[:num2]
            num3 = part.rfind('"links":')
            str2 = part[num3:num2]
            
            data_4.append(str2)
            
            num0 = num1
                    
    return data_5[0:10]


data_6 = []
def m6(mylist):
    """
    
    """
    
    for k in data_4[1]:
        p1 = k.find('"')
        p2 = k.find('"', 1)
           
        link = k[p1+1 : p2]
        links.append(link)

