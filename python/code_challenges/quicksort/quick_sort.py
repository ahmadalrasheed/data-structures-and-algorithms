def QuickSort(arr, left, right):
    if left < right:
        #  Partition the array by setting the position of the pivot value
        position = Partition(arr, left, right)
        #  Sort the left
        QuickSort(arr, left, position - 1)
        #  Sort the right
        QuickSort(arr, position + 1, right)

def Partition(arr, left, right):
    #  set a pivot value as a point of reference
    pivot = arr[right]
    # create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    while right < left:
        # Increment the right pointer till it finds an
        # element greater than  pivot
        while right < len(arr) and arr[right] <= pivot:
            right += 1

        # Decrement the left pointer till it finds an
        # element less than pivot
        while arr[left] > pivot:
            left -= 1


    #  place the value of the pivot location in the middle.
    # all numbers smaller than the pivot are on the left, larger on the right.
    Swap(arr, right, low + 1)

    #  return the pivot index point
    return low + 1

def Swap(arr, i, low):

    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

QuickSort([1,2,3,4] , 0 , 3)
