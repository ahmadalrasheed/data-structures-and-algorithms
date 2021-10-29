from code_challenges.pseudoqueue.PseudoQueue import PseudoQueue
from data_structure.stack_and_queue.stack import Stack
from data_structure.stack_and_queue.queue import Queue

import pytest


# Can successfully push onto a stack
def test_push_into_stack(my_stack):

    #Act
    actual=my_stack.top.value
    expected=7
    #assert
    assert actual==expected


# Can successfully push multiple values onto a stack
def test_push_many_times(my_stack):
    actual1=my_stack.top.value
    actual2=my_stack.top.next.value
    actual3=my_stack.top.next.next.value

    assert actual1==7
    assert actual2==6
    assert actual3==5

# Can successfully pop off the stack
def test_pop_off(my_stack):
    actual=my_stack.top.value
    my_stack.pop()
    actual2=my_stack.top.value
    expected1=7
    expected2=6
    assert actual==expected1
    assert actual2==expected2

# Can successfully empty a stack after multiple pops
def test_empty_stack_after_multiple_pops(my_stack):
    # act
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    actual=my_stack.top
    # assert
    assert actual==None
# Can successfully peek the next item on the stack
def test_peek(my_stack):
    # act
    actual=my_stack.peek()
    expected=7
    # assert
    assert actual==expected
# Can successfully instantiate an empty stack

def test_instantiate_empty_stack():
    my_stack=Stack()
    actual=type(my_stack.top)
    expected=my_stack.top.__class__
    # assert
    assert actual==expected
# Calling pop or peek on empty stack raises exception


#queues
# Can successfully enqueue into a queue
def test_can_enque_to_queue(My_Queue):
    # act
    actual=My_Queue.front.value
    expected=2
    # assert
    assert actual==expected
# Can successfully enqueue multiple values into a queue

def test_enqueue_multiple_times(My_Queue):
    actual1=My_Queue.front.value
    actual2=My_Queue.front.next.value
    actual3=My_Queue.front.next.next.value

    assert actual1==2
    assert actual2==3
    assert actual3==5
# Can successfully dequeue out of a queue the expected value

def test_deque(My_Queue):
    actual=My_Queue.dequeue()
    expected=2

    assert actual==expected

# Can successfully peek into a queue, seeing the expected value
def test_peek_for_queue(My_Queue):
    actual=My_Queue.peek()
    expected=2

    assert actual==expected
# Can successfully empty a queue after multiple dequeues
def test_empty_queue_after_multiple_deques(My_Queue):
    # act
    My_Queue.dequeue()
    My_Queue.dequeue()
    My_Queue.dequeue()
    actual=My_Queue.front
    # assert
    assert actual==None

# Can successfully instantiate an empty queue
def test_instantiate_empty_queue():
    My_Queue=Queue()
    actual=My_Queue.front
    expected=None
    # assert
    assert actual==expected

def test_dequeue_and_peek_on_emty_queue_raise_exeption():
    # arrangement
    My_Queue=Queue()
    actual=My_Queue.peek()
    expected=None

    assert actual==expected



# ---------------------------------------------------------------
# PseudoQueue tests


def test_pseudo_queue_enqueue_value(pseudo_queue_1):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = pseudo_queue_1.front.value

    # Assert
    assert actual == expected


def test_pseudo_queue_enqueue_multiple(pseudo_queue_5):
     # Arrange
    expected_1 = "Test_Value_1"
    expected_2 = "Test_Value_2"

    # Actpseudo_queue_5
    actual_1 = pseudo_queue_5.front.value
    actual_2 = pseudo_queue_5.front.next.value

    # Assert
    assert actual_1 == expected_1
    assert expected_2 == actual_2


def test_pseudo_queue_dequeue_value(pseudo_queue_5):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = pseudo_queue_5.dequeue()

    # Assert
    assert actual == expected


def test_pseudo_queue_dequeue_multiple(pseudo_queue_5):
     # Arrange
    expected = True

    # Act
    pseudo_queue_5.dequeue()
    pseudo_queue_5.dequeue()
    pseudo_queue_5.dequeue()
    pseudo_queue_5.dequeue()
    pseudo_queue_5.dequeue()


    # Assert
    with pytest.raises(Exception):
        assert pseudo_queue_5.dequeue()

        # ---------------------------------------------------

@pytest.fixture
def My_Queue():
    myobject=Queue()
    myobject.enqueue(2)
    myobject.enqueue(3)
    myobject.enqueue(5)
    return myobject

@pytest.fixture
def my_stack():
    myobject=Stack()
    myobject.push(2)
    myobject.push(3)
    myobject.push(5)
    myobject.push(6)
    myobject.push(7)
    return myobject

@pytest.fixture
def pseudo_queue_0():
    pseudo = PseudoQueue()
    return pseudo

@pytest.fixture
def pseudo_queue_1():
    pseudo = PseudoQueue()
    pseudo.enqueue("Test_Value_1")
    return pseudo

@pytest.fixture
def pseudo_queue_5():
    pseudo = PseudoQueue()
    pseudo.enqueue("Test_Value_1")
    pseudo.enqueue("Test_Value_2")
    pseudo.enqueue("Test_Value_3")
    pseudo.enqueue("Test_Value_4")
    pseudo.enqueue("Test_Value_5")
    return pseudo
