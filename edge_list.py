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
def add_id(user_list):
    """
    this creates an id for each user_id in the list user
    it returns a list of lists with an id (int) and user_id. 
    """
    #user is already created at the beginning of this file.
    for i in range(len(user_list)):
        n0 = user_list[i].find(':')
        n1 = user_list[i].find(';')
        part = user_list[i][n0+2:n1-1]
        
        ids.append([i, part])
    
    return ids[0:10]

edge = []
def edgelist(net_list):
    """
    """
    for item in net_list:
        n0 = item.find('[', 1)
        part0 = item[n0+1:]
        n1 = part0.find(']')
        links = part0[:n1]
        
        part1 = part0[n1:]
        n2 = part1.find(':')
        user = part1[n2+1:]
        
        pieces = links.split(',')
        for p in pieces:
            edge.append([user, p])
    
    return edge[0:2]
    
    
        
    