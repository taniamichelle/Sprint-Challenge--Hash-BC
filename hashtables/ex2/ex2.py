#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_retrieve, 
                        hash_table_insert)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        # print('ticket source', tickets[i].source, tickets[i].destination)
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    for j in range(length):
        if route[j-1] is not None:
            route[j] = hash_table_retrieve(hashtable, route[j-1])
    
    return route