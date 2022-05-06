def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    # create for loop
    # loop over value in lst
    # if value is not instance of list
    # return False
    # else return True

    for value in lst:
        if not isinstance(value, list):
            return False
    else:
        return True
