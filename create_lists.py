#program to split a json file exported from mongodb (with mongoexport)
import json
import os

mydata= ['users.json', 'network.json']
#this is the path in the amazon server, where the data is stored.
path1 = os.path.join('/home/ubuntu/lastfm/data', mydata[0])
path2 = os.path.join('/home/ubuntu/lastfm/data', mydata[1])


data_1 = []
data_2 = []
data_3 = []
data_4 = []


def users_1(myfile):
    """
    myfile is the file users.json in path1.
    strips each line in myfile and appends only US users in data_1.
    returns the length of the list.
    """
    
    data_json = open(myfile)
    
    for line in data_json:
        a = line.strip()
        if "US" in a: #this appends only US users.
            data_1.append(a)
    
    data_json.close()
    
    return len(data_1)


def users_2(mylist):
    """
    mylist is list of strings created by the function users_1.
    selects playcount and user_id from mylist to data_2.
    returns the first 10 elements of data_2 .
    """
    
    for i in mylist:
        n0 = i.index('"playcount":')
        part0 = i[n0:]
        s0 = part0.find(':')
        e0 = part0.find(',')
        number = '"playcount":' + part0[s0+1:e0]
        
        n1 = i.index('"user_id":')
        part1 = i[n1:]
        s1 = part1.find(':')
        e1 = part1.find('}')
        user = '"user_id"' + part1[s1+1:e1]
        
        data_2.append(user, number)
    
    fl = open('user_list.txt', 'w')
    for item in data_2:
        fl.write(item + '\n')
    fl.close()
    
    return data_2[0:10]


def network_1(myfile):
    """
    myfile is the file network.json in path2.
    strips each line in myfile and appends links and
    user_id information to data_3.
    returns the length of the list.
    """
    
    data_json = open(myfile)
    
    for line in data_json:
        a = line.strip()
        part = a.find('"links":')
        data_3.append(a[part:])
    
    data_json.close()
    
    return len(data_3)  


def network_2(mylist):
    #WARNING: this function may take up to 20 hours to select US users and their network.
    """
    mylist is the list created by the function network_1.
    converts mylist into a string and seeks each US user in this string.
    Then it appends user_id and lastfm friends to data_4.
    data_4 contains symmetric friendship information for US users
    only(!). It does not collect friendships outside the United States,
    even though this information is available in data_3.
    returns the first elements of data_4. 
    """
    str1 = ''.join(mylist)
    
    names = []
    for i in range(len(data_2)):
        names.append(data_2[i][0])
    
    #shows the first elements in names.
    print names[:2] 
    
    track = range(0,610000, 1000)
    for i in range(len(names)):
        iden = '"user_id":' + names[i]
        user = str1.find(iden)
        n1 = str1.find('}', user)
        
        #the following condition avoids memory errors.
        if n1 > 20000: #this number is arbitrary, but secures enough elements to find '"links":'
            part = str1[user-20000:n1]
        else:
            part = str1[:n1]
        
        n0 = part.rfind('"links":')
        piece = part[n0:n1]
        
        data_4.append(piece)
        
        #tracker
        if i in track:
            print i
    
    #creates a .csv file with the info.
    fl = open('network_list.txt', 'w')
    for item in data_4:
        fl.write(item + '\n')
    fl.close()
    
    return data_4[0:5]
