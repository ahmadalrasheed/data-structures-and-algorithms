
from code_challenges.insertionsort.insertion_sort import InsertionSort



def test_InsertionSort_array_1():
    # act
    actual=InsertionSort([8,4,23,42,16,15])
    expected=[4,8,15,16,23,42]
    #assert
    assert actual == expected

def test_InsertionSort_array_Reverse_sorted():
    # act
    actual=InsertionSort([20,18,12,8,5,-2])
    expected=[-2,5,8,12,18,20]
    #assert
    assert actual == expected
def test_InsertionSort_array_Few_uniques():
    # act
    actual=InsertionSort([5,12,7,5,5,7])
    expected=[5,5,5,7,7,12]
    #assert
    assert actual == expected
def test_InsertionSort_array_Nearly_sorted():
    # act
    actual=InsertionSort([2,3,5,7,13,11])
    expected=[2,3,5,7,11,13]
    #assert
    assert actual == expected
