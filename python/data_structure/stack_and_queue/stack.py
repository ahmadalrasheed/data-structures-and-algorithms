from data_structure.stack_and_queue.node import Node

class EmptyStack(Exception):
    pass

class Stack():
    def __init__(self):
        self.top=None
    def push(self,value):
        """
        This method adds a Node to the top of a Stack.

        Arguments:
        value: any

        """
        node=Node(value)
        node.next=self.top
        self.top=node
    def pop(self):
        """
        This method removes the top Node of a Stack.
        Arguments: None
        Return: Popped Node Value
        """
        try:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value
        except AttributeError as err:
            raise err

    def peek(self):
        """
        This method returns the value of top Node of a Stack.

        Arguments: None

        Return : Top Node Value
        """
        try:
            return self.top.value
        except AttributeError as err:
            raise err
    def is_empty(self):
        """  This method checks if a Stack has any Nodes within.

             Arguments: None

            Return : Boolean
        """
        try:
            return bool(self.top.value)
        except AttributeError as err:
            raise err




