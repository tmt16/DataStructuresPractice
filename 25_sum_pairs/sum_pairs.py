def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    # create length of nums variable
    # create to_return variable
    # create for loop
    # loop over i in range of length of nums - 1
    # create for loop
    # loop over j in range of i in length of nums
    # if nums[i] + nums[j] == goal
    # if distance of j-i is less than length of nums
    # length of nums = j - i
    # save indeces in variable to_return: nums[i], nums[j]
    # if to return != 0
    #  return to_return
    # return () 

    length_of_nums = len(nums)
    to_return = 0

    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == goal:
                if j - i < length_of_nums:
                    length_of_nums = j - i
                    to_return = nums[i], nums[j]

    if to_return != 0:
        return to_return

    return ()


