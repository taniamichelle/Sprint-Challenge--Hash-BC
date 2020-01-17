#  You may not need all of these. Remove unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for weight in weights:
        # index = len(weights)
        index = 0
        value = limit - weight
        ht_val = hash_table_retrieve(ht, weight)

        if weight != ht_val:
            hash_table_insert(ht, weight, value)
            index += 1
        elif weight == ht_val:
            unsorted_index = weights.index(ht_val)
            answer = (index, unsorted_index)
            return answer
    return None

    # for weight in weights:
    #     index = len(weights)
    #     index = 0
    #     difference = limit - weight
    #     value = (index, difference)
    #     ht_val = hash_table_retrieve(ht, weight)

    #     if weight != ht_val[1]:
    #         hash_table_insert(ht, weight, value)
    #         index += 1
    #     elif weight == ht_val[1]:
    #         return (weight[index], ht_val[0])
    # else:
    #     return None


get_indices_of_item_weights([1, 2, 3, 4, 5], 5, 7)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
