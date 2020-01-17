#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


tickets = []


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length  # Amount of inserted tickets

    key = Ticket.source
    tickets.get(key="None")

    for ticket in tickets:
        # index = route[index]
        # index = 0
        key = Ticket.source
        value = Ticket.destination
        hashtable_val = hash_table_retrieve(hash_table, key)

        if key == None:
            hash_table_insert(hashtable, "None", value)
            route += 1  # Update route
        elif key == hashtable_val:
            hash_table_insert(hashtable, key, value)
            route += 1
        else:
            pass

    return route
