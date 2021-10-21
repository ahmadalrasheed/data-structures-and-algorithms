from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        """
        This method adds a Node to the back of a Queue.

        Arguments:
        value: any
        """
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        """
        This method removes a Node to the front of a Queue.
        Arguments: None
        Return: Value of Dequeued Node
        """
        try:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value
        except AttributeError:
            print('The queue is already Empty')


    def peek(self):
        """
        This method returns the value of front Node of a Queue.

        Arguments: None

        Return : Front Node Value
        """
        try:
            return self.front.value
        except AttributeError:
            print('The queue is already Empty')



    def is_empty(self):
        return not self.front
