def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)<1:
        return (0, 0)
    min = ints[0]
    max = ints[0]
    
    for int in ints:
        if int < min:
            min = int
        
        if int > max:
            max = int

    return (min, max)
    
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 10000)]  # a list containing 0 - 9999
random.shuffle(l)

print ("Pass" if ((0, 9999) == get_min_max(l)) else "Fail")

l = [i for i in range(-1000, 10000)]  # a list containing -1000 - 9999
random.shuffle(l)

print ("Pass" if ((-1000, 9999) == get_min_max(l)) else "Fail") #Testing negative numbers

l = [i for i in range(-1000, 1)]  # a list containing -1000 - 0
random.shuffle(l)

print ("Pass" if ((-1000, 0) == get_min_max(l)) else "Fail") #Testing negative numbers and Zero