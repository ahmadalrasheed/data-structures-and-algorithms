"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:

  def __init__(self):
    self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    function to in order the list using Trees
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)

    walk(self.root)
    return list_of_items


# -----------------------------------
# Binary search tree

class BinarySearch(BinaryTree):

    def __init__(self, root=None):
        """
        BinaryTree class creates BinaryTree instances.
        Arguments:
        root: Node
        """
        super().__init__()
        self.target = None


    def add(self, value):
        """
        Adds a new node with that value in the correct location in the binary search tree.
        Arguments:
        value: any
        Return :Added Node Value
        """


        def walk(root, value):
            """
            walk is a helper method for add.
            Arguments:
            root: Tree Root Node
            value: any
            """
            if not root:
                self.target = Node(value)
                root = self.target
                return root

            else:
                if root.data == value:
                    self.target = root
                    return root

                if value > root.data:
                    root.right = walk(root.right, value)

                if value < root.data:
                    root.left = walk(root.left, value)

            return root


        if not self.root:
            self.target = Node(value)
            self.root = self.target
            return self.root
        else:
            walk(self.root, value)
            print(self.target.data)
            return self.target



    def contain(self, value):
        """
        Indicates whether or not a value is in the tree at least once.
        Arguments:
        value: any
        Return :Boolean
        """
        self.target = False

        def walk(root, value):
            """
            walk is a helper method for contain.
            Arguments:
            value: any
            """

            if root and root.data == value:
                self.target = True
                print(self.target)
                return self.target

            if root and value > root.data:
                walk(root.right, value)

            if root and value < root.data:
                walk(root.left, value)

        walk(self.root, value)

        print(self.target)
        return self.target


