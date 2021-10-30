# Stacks and Queues
<!-- Short summary or background information -->
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.Queues is simmilar to stack but with another rules , such as that the first elemnt in the queue to be inserted is the first element to be dequeued , not like the stack in their logic

## Challenge
<!-- Description of the challenge -->
is to build my own stack object and perform on it its methods such as `pop` and `push ` and `peek ` and `is_empty`and to construct my queue object and to build in it their methods such as `enqueue` and `dequeue` and `peek` and `is_empty`

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* BigO complexity for (Stack.push) method:O(1)

* BigO complexity for (Stack.pop) method:O(1)

* BigO complexity for (Stack.peek) method:O(1)

* BigO complexity for (Stack.is_empty) method:O(1)

* BigO complexity for (Queue.queue) method:O(1)

* BigO complexity for (Queue.dequeue) method:O(1)

* BigO complexity for (Queue.peek) method:O(1)

* BigO complexity for (Queue.is_empty) method:O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->

>Stack.push()
        This method adds a Node to the top of a Stack.
        Arguments:
        value: any

>Stack.pop()
        This method removes the top Node of a Stack.
        Arguments: None
        Return: Popped Node Value

>Stack.peek()
        This method returns the value of top Node of a Stack.
        Arguments: None
        Return : Top Node Value

>Stack.is_empty()
            This method checks if a Stack has any Nodes within.
             Arguments: None
            Return : Boolean

>Queue.enqueue()
  This method adds a Node to the back of a Queue.
  Arguments:
  value: any


>Queue.dequeue()
  This method removes a Node to the front of a Queue.
  Arguments: None
  Return: Value of Dequeued Node


>Queue.peek()
  This method returns the value of front Node of a Queue.
  Arguments: None
  Return : Front Node Value

>queue.is_empty()
            This method checks if a queue has any Nodes within.
             Arguments: None
            Return : Boolean

