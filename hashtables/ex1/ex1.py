#  You may not need all of these. Remove unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for weight in weights:
        if weight != ht.key:
            if weight != ht.value[1]:
                hash_table_insert(ht, weight, (weight[index], (limit-weight))
            elif weight == ht.value[1]:
                return (weight[index], ht.value[0])
        else:
            pass
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
