
from data_structure.trees.trees import Queue

def breadth_first(tree):
    """
    A binary tree method which returns a list of items that it contains

    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered
    """
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
    my_node=tree.root
    breadth.enqueue(my_node)

    list_of_items = []

    while breadth.data:
      front = breadth.dequeue()
      list_of_items += [front.data]
      print(list_of_items)

      if front.left:
        print(front.left.data)
        breadth.enqueue(front.left)


      if front.right:
        print(front.right.data)
        breadth.enqueue(front.right)


    return list_of_items
