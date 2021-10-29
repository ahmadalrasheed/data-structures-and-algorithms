from data_structure.stack_and_queue.node import Node
from data_structure.stack_and_queue.stack import Stack




class PseudoQueue():
     """
     Queue class creates a Pseudo Queue instances.
     """
     def __init__(self, front = None, rear = None):
        self.front = front
        self.rear = rear
        self.straight_stack = Stack()
        self.reverse_stack = Stack()


     def enqueue(self, value):
        """
        This method Inserts value into the PseudoQueue
        Arguments:
        value: any
        """
        if not self.front:
            self.reverse_stack.push(value)
            self.front = Node(self.reverse_stack.peek())
            self.rear = self.front
            self.reverse_stack.pop()

        else:
            self.reverse_stack.push(value)

            current = self.reverse_stack.top
            while current:
                self.straight_stack.push(self.reverse_stack.peek())
                self.reverse_stack.pop()
                current = self.reverse_stack.top

            current = self.straight_stack.top
            while current:
                self.rear.next = Node(self.straight_stack.peek())
                self.straight_stack.pop()
                self.rear = self.rear.next
                current = self.straight_stack.top

     def dequeue(self):
        """
        This method Extracts a value from the PseudoQueue
        Arguments: None
        Return: Value of Dequeued Node
        """
        trash = ''
        if not self.front:
            raise Exception("Queue is empty.")

        else:
            current = self.front
            while current:
                self.reverse_stack.push(current.value)
                current = current.next

            current = self.reverse_stack.top
            while current:
                self.straight_stack.push(self.reverse_stack.peek())
                self.reverse_stack.pop()
                current = self.reverse_stack.top

            trash = self.straight_stack.peek()
            self.straight_stack.pop()
            if self.straight_stack.top:
                self.front = Node(self.straight_stack.peek())
            self.rear = self.front
            if self.straight_stack.top:
                self.straight_stack.pop()
                current = self.straight_stack.top
                while current:
                    self.rear.next = Node(self.straight_stack.peek())
                    self.straight_stack.pop()
                    self.rear = self.rear.next
                    current = self.straight_stack.top
            else:
                self.front = None
                self.rear = self.front

            return trash
