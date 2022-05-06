def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    #  create counter variable
    # create for loop
    # loop over num of nums
    # if counter[num]
    # counter += 1
    # if counter[num] is not in nums
    # counter = 1
    # create max of values variable
    # get key of max_value
    # return key of max_value


    counter = {}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    max_value = max(counter.values())
    max_value = max(counter, key=counter.get)
    return max_value

    
    


