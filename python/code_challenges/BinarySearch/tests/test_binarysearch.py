from binarysearch import __version__
from binarysearch.binary_search import binarySearch

def test_version():
    assert __version__ == '0.1.0'

def test_binarySearch():
    predicted=binarySearch([1,2,3,6,9],3)
    actual=2
    assert predicted==actual


