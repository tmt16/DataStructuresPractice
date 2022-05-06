def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    # create for loop 
    # loop over each element in lst
    # if list is > 0 then go to next
    # return 1st[-1:-1]

    for element in lst:
        if len(lst) > 0:
            return lst[-1]

