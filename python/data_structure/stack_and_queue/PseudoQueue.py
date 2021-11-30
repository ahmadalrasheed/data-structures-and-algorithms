from data_structure.stack_and_queue.node import Node
from data_structure.stack_and_queue.stack import Stack
class PseudoQueue():

    def __init__(self):
        self.front=None
        self.rear=None
        self.stack1=Stack()
        self.stack2=Stack()

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
            self.stack1.push(value)
            
