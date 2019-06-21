def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = findPivot(input_list, 0, len(input_list)-1)
    if input_list[pivot] == number:
        return pivot
    elif input_list[pivot] < number:
        return -1
    elif input_list[0] == number:
        return 0
    elif input_list[0] < number:
        return binary_search(input_list, 0, pivot-1, number)
    else:
        return binary_search(input_list, pivot+1, len(input_list)-1, number)

def binary_search(arr, low, high, number):
    targetIndex = -1
    middle = (((high - low)) // 2 + low)
    while high>low:
        if arr[middle] == number:
            targetIndex = middle
            break
        elif arr[middle] < number:
            low = middle + 1
        else:
            high = middle  
        middle = (((high - low)) // 2 + low)
    if arr[middle] == number:
            targetIndex = middle    
    return targetIndex


def findPivot(arr, low, high):
    middle = ((high + low)) // 2

    if low == high:
        return low
        

    if arr[middle] > arr[high] and arr[middle+1] < arr[middle]:
        return middle
    elif arr[middle] < arr[high] and arr[middle-1] > arr[middle]:
        return middle-1
    elif arr[middle] < arr[high]:
        return findPivot(arr, middle+1, high)
    else:
        return findPivot(arr, low, middle-1) 

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])