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

#
ids = []
def add_id():
    """
    this creates an id for each user_id in the list user
    it returns a list of lists with an id (int) and user_id. 
    """
    #user is already created at the beginning of this file.
    for i in range(len(user)):
        n0 = user[i].find(':')
        n1 = user[i].find(';')
        part = user[i][n0+2:n1-1]
        
        ids.append([i, part])
    
    return ids[0:10]

network_list = []
def edgelist():
    """
    """
    for item in network:
        n0 = item.find('[', 1)
        part0 = item[n0+1:]
        n1 = part0.find(']')
        links = part0[:n1]
        
        part1 = part0[n1:]
        n2 = part1.find(':')
        user = part1[n2+1:]
        
        network_list.append([users, links.split(',')])
        

    
    
        
    