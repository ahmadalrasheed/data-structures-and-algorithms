"""
Tests for Binary Tree
"""

from data_structure.trees.trees import BinaryTree, Node , BinarySearch
import pytest




# Can successfully instantiate an empty tree
def test_can_instantiate_emty_tree():
    # arrange

    tree = BinaryTree()
    expected=None
    # act

    actual=tree.root
    assert actual==expected
# Can successfully instantiate a tree with a single root node
def test_can_instantiate_tree_with_single_root_node():
    # arrange

    tree = BinaryTree()
    My_root=Node('5')
    tree.root=My_root.data
    # act

    expected='5'
    actual=tree.root
    assert actual==expected


#  Can successfully add a left child and right child to a single root node
def test_can_add_left_and_right_to_root():
    # arrange

    tree = BinaryTree()
    My_root = Node('5')
    My_root.left = Node('6')
    My_root.right = Node('8')
    tree.root=My_root
    # act

    expected1='5'
    expected2='6'
    expected3='8'
    actual1=tree.root.data
    actual2=tree.root.left.data
    actual3=tree.root.right.data
    assert actual1==expected1
    assert actual2==expected2
    assert actual3==expected3

#  Can successfully return a collection from a breadth traversal


def test_bfs():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('A')
  b_node = Node('B')
  c_node = Node('C')
  d_node = Node('D')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["A", "B", "C", "D"]
  # set actual to return data of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs passed")


#  Can successfully return a collection from a breadth traversal

def test_bfs_2():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "3", "4"]
  # set actual to return data of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs_2 passed")



#  Can successfully return a collection from a preorder traversal

def test_pre_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "4", "3"]
  # set actual to return data of pre_order call
  actual = tree.pre_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_pre_order_ passed")


#  Can successfully return a collection from a postorder traversal


def test_post_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["4", "2", "3", "1"]
  # set actual to return data of post_order call
  actual = tree.post_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")



#  Can successfully return a collection from an inorder traversal


def test_in_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["4", "2", "1", "3"]
  # set actual to return data of in_order call
  actual = tree.in_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_in_order_ passed")



# ------------------------------
# tests for binary search




def test_bs_tree_add(bs_tree):
    #Arrange

    expected = 1

    #Act
    node = bs_tree.add(1)
    actual = node.data

    #Assert
    assert actual == expected


def test_bs_contain_add(bs_tree):
    #Arrange

    expected = True

    #Act
    bs_tree.add(1)
    actual = bs_tree.contain(1)

    #Assert
    assert actual == expected

def test_bs_not_contain(bs_tree):
    #Arrange

    expected = False

    #Act
    actual = bs_tree.contain(1)

    #Assert
    assert actual == expected

def test_bs_contain_right(bs_tree):
    #Arrange

    expected = True

    #Act
    actual = bs_tree.contain(80)

    #Assert
    assert actual == expected

def test_bs_add_correct_location(bs_tree):
    #Arrange

    expected = 100

    #Act
    bs_tree.add(100)
    actual = bs_tree.root.right.right.right.right.data

    #Assert
    assert actual == expected

def test_bs_add_empty():
    #Arrange
    bs_tree = BinarySearch()
    expected = 1

    #Act
    bs_tree.add(1)
    actual = bs_tree.root.data

    #Assert
    assert actual == expected


@pytest.fixture
def bs_tree():

    node50 = Node(50)

    node45 = Node(45)
    node40 = Node(40)
    node35 = Node(35)
    node30 = Node(30)
    node20 = Node(20)

    node80 = Node(80)
    node70 = Node(70)
    node65 = Node(65)
    node60 = Node(60)
    node55 = Node(55)


    node50.left = node40
    node50.right = node60

    node40.left = node30
    node40.right = node45

    node30.left = node20
    node30.right = node35

    node60.left = node55
    node60.right = node70

    node70.left = node65
    node70.right = node80

    bs_tree = BinarySearch()
    bs_tree.root = node50

    return bs_tree
