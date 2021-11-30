import re
from code_challenges.hashtable.hash_table import HashTable

def repeated_word(my_string):
  """
  Function to find the first word to occur more than once in a specific string

  Arguments:
  input->string
  Output->string
  """
  my_object=HashTable()
  my_string = my_string.lower()
  word_list=re.split(' |, ', my_string)

  for item in word_list:
    if my_object.contains(item):
      item_value=my_object.get(item)
      item_value=item_value + 1
      my_object.add(item,item_value)
    else:
      my_object.add(item,1)
    if my_object.get(item) == 2:
      return item

  return None
