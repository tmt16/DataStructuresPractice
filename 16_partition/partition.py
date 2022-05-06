def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    # create true_list variable
    # create false_list variable
    # loop over each value in lst
    # if value of fn is true
    # append value to true_list
    # if value of fn is not true
    # append value to false_list
    # return list of true_list and false_list

    true_list = []
    false_list = []
    
    for value in lst:
        if fn(value):
            true_list.append(value)
        if not fn(value):
            false_list.append(value)
    return [true_list, false_list]

        

