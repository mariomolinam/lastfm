#This file creates an edge list with the network information from lastfm users.

#open files and make them readable lists.
user = []
f1 = open('user_list.txt')
for item in f1:
    user.append(item.strip('\n'))
f1.close()

network = []
f2 = open('network_list.txt')
for item in f2:
    network.append(item.strip('\n'))
f2.close()


def add_id(mylist):
    """
    this creates an id for each user_id in the list user
    it returns a list of lists with an id (int) and user_id. 
    """
    
    ids = []
    
    for i in range(len(mylist)):
        n0 = mylist[i].find(':')
        n1 = mylist[i].find(';')
        part = mylist[i][n0+2:n1-1]
        
        ids.append([i, part])
        
        
def edgelist():
    """
    """
    
    
        
    