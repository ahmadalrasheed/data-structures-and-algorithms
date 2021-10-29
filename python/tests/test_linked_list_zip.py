from code_challenges.linked_list.linked_list import LinkedList
from code_challenges.linked_list_zip.linked_list_zip import zip_Lists
# from code_challenges.linked_list.linked_list import Node


def test_linked_list_zip():
  #Arrange
    list1 = LinkedList()
    list1.insert("a")
    list1.append("b")
    list1.append("c")
    list2 = LinkedList()
    list2.insert("m")
    list2.append("l")
    list2.append("n")

    expected = " a -> m -> b -> l -> c -> n ->"

    #Act
    actual = zip_Lists(list1, list2)

    #Assert
    assert actual == expected


def test_linked_list_zip_list1_longer():
      #Arrange
    list1 = LinkedList()
    list1.insert("a")
    list1.append("b")
    list1.append("c")
    list1.append("d")
    list2 = LinkedList()
    list2.insert("m")
    list2.append("l")
    list2.append("n")

    expected = " a -> m -> b -> l -> c -> n -> d ->"

    #Act
    actual = zip_Lists(list1, list2)

    #Assert
    assert actual == expected


def test_linked_list_zip_list2_longer():
    #Arrange
    list1 = LinkedList()
    list1.insert("a")
    list1.append("b")
    list1.append("c")

    list2 = LinkedList()
    list2.insert("m")
    list2.append("l")
    list2.append("n")
    list2.append("x")
    list2.append("y")

    expected = " a -> m -> b -> l -> c -> n -> x -> y ->"

    #Act
    actual = zip_Lists(list1, list2)

    #Assert
    assert actual == expected

def test_linked_list_zip_list1_1():
       #Arrange
    list1 = LinkedList()
    list1.insert("a")


    list2 = LinkedList()
    list2.insert("m")
    list2.append("l")
    list2.append("n")


    expected = " a -> m -> l -> n ->"

    #Act
    actual = zip_Lists(list1, list2)

    #Assert
    assert actual == expected

def test_linked_list_zip_list2_1():
    #Arrange
    list1 = LinkedList()
    list1.insert("a")
    list1.append("c")
    list1.append("b")


    list2 = LinkedList()
    list2.insert("m")


    expected = " a -> m -> c -> b ->"

    #Act
    actual = zip_Lists(list1, list2)

    #Assert
    assert actual == expected


def test_linked_list_zip_reverse_order():
    #Arrange
    list1 = LinkedList()
    list1.insert("1")
    list1.append("4")
    list1.append("7")
    list2 = LinkedList()
    list2.insert("A")
    list2.append("D")
    list2.append("G")

    expected = " A -> 1 -> D -> 4 -> G -> 7 ->"

    #Act
    actual = str(zip_Lists(list2, list1))

    #Assert
    assert actual == expected
