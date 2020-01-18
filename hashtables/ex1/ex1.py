#  You may not need all of these. Remove unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Iterate through `weights` list:
    for i in weights:
        # Define `weight` as current weight
        weight = weights[i]
        # # Calculate limit-weight + store as `difference`
        # difference = limit - weight
        # Define `value` as a tuple: (curr index, difference)
        # value = (i, difference)

        print(f"weight: {weight}")

        # If weight not in ht:
        if weight not in ht:
            # Add key:weight + value:(its_index, difference) to ht
            hash_table_insert(ht, weight, i)
        # If weight IS in ht:
        else:
            pass

    # Iterate through ht
    for j in ht:
        ht_val = hash_table_retrieve(ht, weight)
        # Compare j to limit - j
        if j == (limit - j):
            # Retrieve ht_value
            return ht_val
        else:
            pass

    return None


get_indices_of_item_weights([1, 2, 3, 4, 5], 5, 7)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
