def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 3:
        return input_list
    
    sortedList = mergeSort(input_list, 0, len(input_list) - 1)
    numOne = ''
    numTwo = ''

    for i in range(0, len(sortedList)):
        if i % 2 == 0:
            numOne = numOne + str(sortedList[len(sortedList) - 1 - i])
        else:
            numTwo = numTwo + str(sortedList[len(sortedList) - 1 - i])

    return [int(numOne), int(numTwo)]

def mergeSort(arr, beg, end):
    diff = end - beg
    if diff == 1:
        return combineLists([arr[beg]], [arr[end]])
    elif diff <= 0:
        return [arr[beg]]
    else:
        middle = (end - beg) // 2 + beg
        leftArray = mergeSort(arr, middle+1, end)
        rightArray = mergeSort(arr, beg, middle)
        return combineLists(leftArray, rightArray)

        
def combineLists(arr1, arr2):
    
    returnArray = []
    firstIndex = 0
    secondIndex = 0
    while firstIndex < len(arr1) and secondIndex < len(arr2):
        if arr1[firstIndex] < arr2[secondIndex]:
            returnArray.append(arr1[firstIndex])
            firstIndex = firstIndex + 1
        else:
            returnArray.append(arr2[secondIndex])
            secondIndex = secondIndex + 1
    
    if firstIndex < len(arr1):
        for i in range(firstIndex, len(arr1)):
            returnArray.append(arr1[i])
    else:
        for i in range(secondIndex, len(arr2)):
            returnArray.append(arr2[i])            
    return returnArray


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 0, 0, 0, 1, 1], [1000, 100]])
test_function([[0, 0, 0, 0, 0, 0, 1], [1000, 0]])