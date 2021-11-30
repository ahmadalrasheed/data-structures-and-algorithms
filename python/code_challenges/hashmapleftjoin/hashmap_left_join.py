"""This module contains hashmap_left_join function"""

from code_challenges.hashtable.hash_table import HashTable

def hashmap_left_join(hashmap1: HashTable, hashmap2: HashTable):
    """
    hashmap_left_join returns all data from the first hashmap, even if there are no matches in the right table. If it has matches on the second hashmap, it'll return the values along with the corresponding data from the first hashmap, if not, they'll be replaced by None.
    Arguments:
        hashmap1: HashTable
        hashmap2: HashTable
    Return: List of lists containing the joined values.
    """


    try:
        output_list = []

        left_list = hashmap1.keys()

        for key in range(len(left_list)):

            if hashmap2.contains(left_list[key]):
                output_list += [[left_list[key], hashmap1.get(left_list[key]), hashmap2.get(left_list[key])]]

            else:
                if left_list[key]:
                    output_list += [[left_list[key],  hashmap1.get(left_list[key]), None]]

        return(output_list)

    except:

        raise Exception('Please check the hashmaps you entered and try again.')
