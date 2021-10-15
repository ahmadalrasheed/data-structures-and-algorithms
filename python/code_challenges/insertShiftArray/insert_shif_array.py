myarr=[1,2,3,4]

def insertShiftArray(arr,b):
    """
    this function will remove an element from the middle index and shifts other elements in the array to fill the new gap.
    input: array and a value
    output: same array with the value added to its middle
    """
    li=[b]
    a=len(arr)
    if a % 2==0:
        middleindex1=int(a/2)
        newarr=arr[0:middleindex1]+li+arr[middleindex1:]
    elif a % 2 !=0:
        middleindex2=int(round(a/2))
        newarr=arr[0:middleindex2+1]+li+arr[middleindex2+1:]
    return newarr

print(insertShiftArray(myarr,99))
