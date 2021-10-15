
def binarySearch(my_list, low, high, key):

    '''
    this function takes four arguments (sorted list and low value and high value and  search key) and return the index value of the key if the key is in the list
    if the key is not in the list it will return -1
    
    '''

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if my_list[mid] == key:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif my_list[mid] > key:
            return binarySearch(my_list, low, mid - 1, key)

        # Else the element can only be present in right subarray
        else:
            return binarySearch(my_list, mid + 1, high, key)

    else:
        # Element is not present in the array
        return -1

