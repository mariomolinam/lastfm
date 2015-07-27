#This file creates an edge list with the network information from lastfm users.

#open files and make them readable lists.
user = []
f1 = open('users_list.txt')
for item in f1:
    user.append(item.strip('\n'))

network = []
f2 = open('network_list.txt')
for item in f2:
    network.append(item.strip('\n'))

