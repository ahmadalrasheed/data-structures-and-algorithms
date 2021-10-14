

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

  def __init__(self, data, next_ = None):
    self.data = data
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
    if self.head==None:
        return -1
    else:
        self.current=self.head
        while self.current:
            if self.current.data==value:
                return True
            else :
                self.current=self.current.next
        return False

# element1=Node(1)
# print(type(element1).__name__)
ll=LinkedList()
inserted_value=ll.insert(1)
print(inserted_value)
inserted_value=ll.insert(3)
print(inserted_value)
check_if_include=ll.includes(3)
print(check_if_include)
