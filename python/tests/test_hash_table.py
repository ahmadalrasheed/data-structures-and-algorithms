from attr import has
from code_challenges.hashtable.hash_table import HashTable
import pytest

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
    # actual
	expected = 700
	actual = hashtable._HashTable__hash("d")
    #assert
	assert actual == expected

def test_hash_word(hashtable):
    # actual
    expected = 376
    actual =  hashtable._HashTable__hash("dd")
    #assert
    assert actual == expected

def test_hash_get_when_the_key_dont_exist(hashtable):
    # actual
	expected = None
	actual =  hashtable.get("ff")
    #assert
	assert actual == expected
def test_hash_get_when_the_key_exist(hashtable):
    #arrange
    hash_table=hashtable
    hash_table.add('ff',99)
    #actual
    actual=hash_table.get('ff')
    expected=99
    # assert
    assert actual == expected
def test_handle_a_collision_within_the_hashtable(hashtable):
    #arrange
    hash_table1=hashtable

    hash_table1.add('ff',99)
    hash_table1.add('ff',109)
    hash_table1.add('ff',210)
    #actual
    actual=hash_table1.get('ff')
    expected=210
    # assert
    assert actual == expected
def test_retrive_value_from_collision_bucket(hashtable):
    #arrange
    hash_table1=hashtable

    hash_table1.add('ff',99)
    hash_table1.add('ff',109)

    #actual
    actual=hash_table1.get('ff')
    expected=109
    # assert
    assert actual == expected
def test_result_of_hashing_is_in_range_value(hashtable):
    #actual


    actual1 =  hashtable._HashTable__hash('d')
    actual2 =  hashtable._HashTable__hash('hdgd')
    actual3 =  hashtable._HashTable__hash('kskjhshs')
    actual4 =  hashtable._HashTable__hash('llskskssksd')

    #expected
    expected = len(hashtable._HashTable__buckets)

    #assert
    assert actual1 <= expected
    assert actual2 <= expected
    assert actual3 <= expected
    assert actual4 <= expected















