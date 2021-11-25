from data_structure.trees.trees import Node , BinaryTree
from code_challenges.tree_intersection.tree_intersection import tree_intersection
import pytest


def test_tree_intersection1():
    ## arrange
    ## first tree
    tree1 = BinaryTree()

    node1=Node(4)
    node2=Node(5)
    node3=Node(3)
    node4=Node(6)

    node1.right = node2
    node1.left = node3
    node2.right = node4

    tree1.root = node1
    # second tree
    tree2 = BinaryTree()

    node12=Node(4)
    node22=Node(5)
    node32=Node(2)
    node42=Node(8)

    node12.right = node22
    node12.left = node32
    node22.right = node42

    tree2.root = node12

    expected = [4,5]
    actual = tree_intersection(tree1,tree2)
    assert actual == expected

def test_tree_intersection2():
    ## arrange
    ## first tree
    tree1 = BinaryTree()

    node1=Node(4)
    node2=Node(5)
    node3=Node(10)
    node4=Node(11)

    node1.right = node2
    node1.left = node3
    node2.right = node4

    tree1.root = node1
    # second tree
    tree2 = BinaryTree()

    node12=Node(4)
    node22=Node(2)
    node32=Node(2)
    node42=Node(1)

    node12.right = node22
    node12.left = node32
    node22.right = node42

    tree2.root = node12


    actual = tree_intersection(tree1,tree2)
    expected = [4]
    assert actual == expected

def test_tree_intersection3():
    ## arrange
    ## first tree
    tree1 = BinaryTree()

    node1=Node(4)
    node2=Node(5)
    node3=Node(3)
    node4=Node(6)

    node1.right = node2
    node1.left = node3
    node2.right = node4

    tree1.root = node1
    # second tree
    tree2 = BinaryTree()

    node12=Node(4)
    node22=Node(5)
    node32=Node(3)
    node42=Node(6)

    node12.right = node22
    node12.left = node32
    node22.right = node42

    tree2.root = node12


    actual = tree_intersection(tree1,tree2)
    expected = [4,3,5,6]
    assert actual == expected

def test_tree_is_empty():
    ## arrange
    ## first tree
    tree1 = BinaryTree()
    # second tree
    tree2 = BinaryTree()


    # Assert
    with pytest.raises(Exception):
        assert tree_intersection(tree1, tree2)


