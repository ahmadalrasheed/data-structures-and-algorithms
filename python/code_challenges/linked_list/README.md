# Singly Linked List
<!-- Short summary or background information -->
 a linked list is a string of nodes, sort of like a string of pearls, with each node containing both data and a reference to the next node in the list
## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. and add `insert` and `includes` and  `to string` methods and `append` and `insert_before` and `insert_after` and `kth_From_End`
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* time and complexity for (insert) method: O(1)

* time complexity for (includes and to_string) methods: O(n)

* O time complexity for (append) method: O(n)

* O time complexity for (insert_before): O(n)

* O time complexity for (insert_after) : O(n)

* O time complexity for (kth_From_End) : O(n)



## API
<!-- Description of each method publicly available to your Linked List -->
>insert :
""""
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down
    arguments:
    value : any
    returns: None
"""

>includes :
"""
         Indicates whether that value exists  in a linked list
         -----------------------
        Arguments:
        value: any
        Return: Boolean(True or false)
"""

>to-string
"""
        Returns a formatted string representing all the values in the Linked List.
        Arguments:
        None
        Return: String Output
        """
"""

>append
"""
        Adds a new node with the given value to the end of the list
        ---------------
        Arguments:
        value: any
        Return: None
 """

>insert_before
         Adds a new node  immediately before the first node that has the value specified (input value).
        -----------------
        Arguments:
        value: any
        new_value: any
        Return: None
        """



>insert_after
        """
        Adds a new node  immediately after the first node that has the value specified (input value)
        -----------------------------
        Arguments:
        value: any
        new_value: any
        Return: None
        """


>kth_From_End
        a function which is responsible for returning the k-th value from the end of a linked list.
        it Return the node’s value that is k places from the tail of the linked list.
        -----------------------------
        Arguments:
        k: int
        Return: int if the method finds the value or 'Exception' if it doesn't find it
