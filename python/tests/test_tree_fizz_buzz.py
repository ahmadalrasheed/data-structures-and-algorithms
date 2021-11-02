from code_challenges.treefizzbuzz.kary_tree import KaryNode, KaryTree
from code_challenges.treefizzbuzz.tree_fizz_buzz import fizz_buzz

import pytest
def test_k_tree_create_tree():
    #Arrange
    tree = KaryTree(1)
    expected = None

    #Act
    actual = tree.traverse_kary_tree()

    #Assert
    assert actual == expected



def test_k_tree_add_root():
    #Arrange
    k_tree = KaryTree(1)
    k_tree.root = KaryNode(1)
    expected = 1

    #Act
    actual = k_tree.root.value

    #Assert
    assert actual == expected






def test_k_tree_exceptions():
    #Arrange
    k_tree = KaryTree(1)

    #Assert
    with pytest.raises(Exception):
        assert k_tree.traverse_kary_tree()



# K-ary Tree FizzBuzz
# -------------------------------------------------------------------



def test_k_tree_fizz_buzz():
    #Arrange
    k_tree = KaryTree(1)

    #Assert
    with pytest.raises(Exception):
        assert k_tree.traverse_kary_tree()



# @pytest.fixture
# def k_tree():

#     node5 = KaryNode(5)

#     node10 = KaryNode(10)
#     node33 = KaryNode(33)
#     node20 = KaryNode(20)

#     node15 = KaryNode(15)
#     node85 = KaryNode(85)
#     node80 = KaryNode(80)

#     node1 = KaryNode(1)
#     node222 = KaryNode(222)
#     node131 = KaryNode(131)

#     nodeNO = KaryNode("NO")

#     node5.children.append(node10)
#     node5.children.append(node33)
#     node5.children.append(node20)

#     node10.children.append(node15)
#     node10.children.append(node85)
#     node10.children.append(node80)

#     node80.children.append(node1)
#     node80.children.append(node222)
#     node80.children.append(node131)

#     node20.children.append(nodeNO)

#     k_tree = KaryTree(3)
#     k_tree.root = node5

#     return k_tree
# def test_k_tree(k_tree):

#     #Arrange
#     expected = [5, 10, 33, 20, 15, 85, 80, "NO" , 1, 222, 131]


#     #Act
#     actual = k_tree.traverse_kary_tree()

#     #Assert
#     assert actual == expected


# def test_k_tree_fizz_buzz_values(k_tree):
#     #Arrange
#     expected = ["Buzz", "Buzz", "Fizz", "Buzz", "FizzBuzz", "Buzz", "Buzz", "NO" , "1", "Fizz", "131"]

#     #Act
#     actual = fizz_buzz(k_tree)


#     #Assert
#     assert actual == expected
