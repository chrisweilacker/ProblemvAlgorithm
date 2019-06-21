def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<0:
        return -1
    elif number <= 1:
        return number

    # returnNum = 1
    # squared = returnNum ** 2

    # while squared != number and not (squared < number and (returnNum+1)**2 > number):
    #     returnNum = returnNum + 1
    #     squared = returnNum ** 2

    start = 0
    end = number // 2
    middle = (end - start) // 2 + start

    while start<end:
        squared = middle ** 2

        if (squared == number or (squared < number and (middle + 1) ** 2)>number):
            return middle

        if (squared>number):
            end = middle
        else:
            start = middle + 1
        middle = (end-start) // 2 + start
        


    return -1
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")