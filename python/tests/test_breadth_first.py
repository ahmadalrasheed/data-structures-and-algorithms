from code_challenges.breadthfirst.breadth_first import breadth_first
from data_structure.trees.trees import  BinaryTree , Node



def test_breadth_first1():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    d_node = Node(4)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root=a_node

    # set expected list
    expected = [1, 2, 3, 4]
    # set actual to return data of bfs call
    actual = breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected

def test_breadth_first2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(4)
    d_node = Node(6)
    e_node = Node(8)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right=e_node
    # Add Root node to tree
    tree.root=a_node

    # set expected list
    expected = [1, 2, 4, 6 , 8]
    # set actual to return data of bfs call
    actual = breadth_first(tree)
    # assert actual is same as expected
    assert actual == expected

