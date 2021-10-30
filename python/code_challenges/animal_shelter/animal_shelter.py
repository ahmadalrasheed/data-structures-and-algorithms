from data_structure.stack_and_queue.node  import Node
# from node  import Node

class AnimalShelter:
    def __init__(self,front=None,rear=None):
            self.front=front
            self.rear=rear
    def enqueue(self,animal):
        if animal.__class__.__name__=='Dog' or animal.__class__.__name__=='Cat':
            if not self.front:
                self.front=Node(animal.animal_name)
                self.rear=self.front
            else :
                self.rear.next=Node(animal.animal_name)
                self.rear=self.rear.next

    def dequeue(self,pref):
        trash=''
        if pref.__class__.__name__=='Dog' or pref.__class__.__name__=='Cat':
            temp=self.front
            prev=self.front
            if not self.front:
                raise Exception('The queue is empty')
            if pref.animal_name.lower() == self.front.value:
                temp=self.front
                self.front=self.front.next
                temp.next=0
                return temp.value
            counter=0
            while temp.value != pref.animal_name.lower():
                temp=temp.next
                counter+=1
            for _ in range(counter-1):
                prev=prev.next
            trash=temp.value
            prev.next=temp.next
            temp.next=None
        return trash
    def print_queue(self):
        current=self.front
        output=''
        while current:
            output+=f' {current.value}-> '
            current=current.next
        return output





class Dog:
    def __init__(self,animal_name='dog'):
        self.animal_name=animal_name


class Cat:
    def __init__(self,animal_name='cat'):
        self.animal_name=animal_name

class Lion:
    def __init__(self,animal_name='lion'):
        self.animal_name=animal_name

