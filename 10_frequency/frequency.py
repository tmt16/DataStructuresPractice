def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    # create counter variable = 0
    # create for loop
    # loop over each num in lst
    #  if search_term == num
    #  counter += 1
    # return counter

    counter = 0

    for num in lst:
        if search_term == num:
            counter += 1
    return counter