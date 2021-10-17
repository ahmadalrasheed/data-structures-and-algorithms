

class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

  """

  def __init__(self, value, next_ = None):
    self.value = value
    self.next = next_

class LinkedList:
  """
  A class for creating instances of a Linked List.

  Data and other attributes defined here:

  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):
    self.head = None
    self.current=self.head


  def insert(self, value):
    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
    # create new node
    self.head = Node(value, self.head)
    self.current=self.head


  def includes (self,value):
    """
         Indicates whether that value exists  in a linked list
         -----------------------
        Arguments:
        value: any
        Return: Boolean(True or false)
    """
    if self.head==None:
        return -1
    else:
        self.current=self.head
        while self.current:
            if self.current.value==value:
                print(f"Flag :{self.current.value} ")
                return True
            else :
                self.current=self.current.next
        return False

  def __str__(self):
        """
        Returns a formatted string representing all the values in the Linked List.
        Arguments:
        None
        Return: String Output
        """
        self.current = self.head

        output = ""

        while self.current != None:
            print("PRINT", self.current.value)
            output = output + (f"{ {self.current.value} } -> ")
            self.current = self.current.next
        output = output + "NULL"
        return(output)
# element1=Node(1)
# print(type(element1).__name__)
if __name__=="__main__":

    ll=LinkedList()
    inserted_value=ll.insert(1)
    print(inserted_value)
    inserted_value=ll.insert(3)
    print(inserted_value)
    check_if_include=ll.includes(1)
    print(check_if_include)
    print(ll.__class__)
