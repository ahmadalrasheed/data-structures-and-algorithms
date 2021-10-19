
def binarySearch(my_list, key):

    '''
    this function takes four arguments (sorted list and low value and high value and  search key) and return the index value of the key if the key is in the list
    if the key is not in the list it will return -1

    '''
    low=0
    high=len(my_list)-1
    mid=0
    # Check base case
    while low<=high:
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if my_list[mid] == key:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif my_list[mid] > key:
                high=mid-1

            # Else the element can only be present in right subarray
            elif my_list[mid] < key :
                low=mid+1

            else:
            # Element is not present in the array
                return mid
    return(-1)

