# HashMap left Join
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge
<!-- Description of the challenge -->
Write a function that LEFT JOINs two hashmaps into a single data structure.
Write a function called left join
Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big(O) time complexity : O(n)
Big(O) space complexity :O(n)



## API
<!-- Description of each method publicly available in each of your hashtable -->

>hashmap_left_join"""
    hashmap_left_join returns all data from the first hashmap, even if there are no matches in the right table. If it has matches on the second hashmap, it'll return the values along with the corresponding data from the first hashmap, if not, they'll be replaced by None.
    Arguments:
        hashmap1: HashTable
        hashmap2: HashTable
    Return: List of lists containing the joined values.
    """






