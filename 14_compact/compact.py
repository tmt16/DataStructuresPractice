def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # create new_list variable
    # create for loop
    # loop over each element in lst
    # if element == False
    # append element to new_list
    # return new_list

    new_list = []

    for element in lst:
        if element:
            new_list.append(element)
    return new_list