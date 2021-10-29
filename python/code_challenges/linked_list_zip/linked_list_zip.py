from code_challenges.linked_list.linked_list import LinkedList


def zip_Lists(list1, list2):
    """
    Returns the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    Arguments:
    list1: LinkedList
    list2: LinkedList
    Return: LinkedList
    """
    new_list = LinkedList()
    list1.current = list1.head
    list2.current = list2.head

    while list1.current or list2.current:
        if list1.current == list1.head:
            new_list.insert(list1.current.value)
            list1.current = list1.current.next
            new_list.append(list2.current.value)
            list2.current = list2.current.next

        if list1.current:
            new_list.append(list1.current.value)
            list1.current = list1.current.next

        if list2.current:
            new_list.append(list2.current.value)
            list2.current = list2.current.next

    return new_list.printList()






