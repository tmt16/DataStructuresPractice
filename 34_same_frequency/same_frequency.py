from itertools import zip_longest


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # convert strings into 2 lists for each num
    # create 2 dictionary variables for each num
    # convert into 2 dictionaries:
    #  for item in list1/list2
    #  if item in counter1/2
    #   counter[item] += 1
    #   else:
    #   counter[item]
    # if counter1 == counter 2
    #  return True
    # else return False

    list1 = [int(item) for item in str(num1)]
    list2 = [int(item) for item in str(num2)]

    counter1 = {}
    counter2 = {}

    for item in list1:
        if item in counter1:
            counter1[item] += 1
        else:
            counter1[item] = 1
        
    for item in list2:
        if item in counter2:
            counter2[item] += 1
        else:
            counter2[item] = 1
    
    if counter1 == counter2:
        return True
    else:
        return False
