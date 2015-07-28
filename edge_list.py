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


def edgelist():
    pass