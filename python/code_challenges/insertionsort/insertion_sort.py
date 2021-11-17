def InsertionSort(my_arr):
    """
    Function to sort arrays from the smaller value to the largest value
    arguments:
    input->array
    output->soted array
    """
    i = 1
    arr_length=len(my_arr)
    for i  in range(arr_length):
        i=i+1
        j = i - 1
        if i < arr_length :
            temp = my_arr[i]

            while j >= 0 and temp < my_arr[j]:
                my_arr[j + 1] = my_arr[j]
                j = j - 1

            my_arr[j + 1] = temp
    return my_arr

