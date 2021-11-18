# Hashtables
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge
<!-- Description of the challenge -->
The challenege is to create your own hashtable from scratch, so that you can covert a specific key to integer and consider it as the index that you will save this value at , in addition , you have to add specific key to specific location , and also get this value of the key when the key is provided , the hashtable structure is array that contains linkedlists , every value in this array must be None, or linked list that contains key and value pairs


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time comlexity for get method : O(n)
space comlexity for get method : O(1)
Time comlexity for add method : O(1)
space comlexity for add method : O(1)
Time comlexity for _hash function : O(1)
space comlexity for _hash function : O(1)
Time comlexity for insert method : O(1)
space comlexity for insert method : O(1)


## API
<!-- Description of each method publicly available in each of your hashtable -->

>get method :"""  Retrieve the most recent value of in oour hasmap for the given key
      :param key str
      :rvalue any
      """


>add method :"""
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.
        Arg: Takes the key and value
        Return : No return value
        """

>_hash function :        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """


>insert method for linkedlist :       """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """




