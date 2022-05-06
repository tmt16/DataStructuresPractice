def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    # create counter variable
    # create for loop
    # loop over num of nums
    # if num < num:
    # counter += 1
    # return counter

    # counter = 0

    # for num in nums:
    #     for i in len(nums) - 1
    #     if num > num + 1:
            # counter = counter + 1
        # if nums.index(num) == len(nums):
            # print(nums[num])
    # return counter

    counter = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                counter += 1

    return counter
