from code_challenges.BinarySearch.binary_search import binarySearch


def test_binarySearch():
    arr=[4, 8, 15, 16, 23, 42]
    x=15
    expected=2
    actual=binarySearch(arr, 0,len(arr)-1, x)
    assert actual==expected

