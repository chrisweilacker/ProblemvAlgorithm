def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #Testing if input is correct, for negative values and returning correct values for number if it is 1 or 0.  
    if type(number) != int:
        return -1
    elif number<0:
        return -1
    elif number == 1 or number == 0:
        return number

    #The simple solution not utilizing a binary search
    # returnNum = 1
    # squared = returnNum ** 2

    # while squared != number and not (squared < number and (returnNum+1)**2 > number):
    #     returnNum = returnNum + 1
    #     squared = returnNum ** 2

    #Search for the value with a Binary search any number above one will be lower than half the number

    low = 0
    high = number // 2
    middle = (high - low) // 2 + low

    while low < high:
        squared = middle ** 2

        #test if our middle is the floored sqrt of the number
        if (squared == number or (squared < number and (middle + 1) ** 2)>number):
            return middle

        #The number was too high so reduce the top end of the search
        if (squared>number):
            high = middle
        else:
            #number was lower so increase the lower end of the range
            low = middle + 1
        #Reset our test in the middle
        middle = (high-low) // 2 + low
        

    #Should never reach here but if it did return -1
    return -1
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")