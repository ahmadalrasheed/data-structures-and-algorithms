
def binarySearch(my_list,key):
    '''
    this function takes two arguments (sorted list and search key) and return the index value of the key if the key is in the list
    if the key is not in the list it will return -1
    '''
    index=0
    for i in my_list:
        if i==key:
            return index
        index+=1
    for y in my_list :
        if y!=key:
            return -1

print(binarySearch([1,2,3,6,9],9))

