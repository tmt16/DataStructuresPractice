def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    # if end is empty
    #  end = length of nums
    # return 
    # sum of nums using slicing[start:end + 1]
    
    if end is None:
        end = len(nums)

    return sum(nums[start:end + 1])


    # 2nd Partial Solution:

    # sum = 0

    # if start and not end:
    #     for num in nums:
    #         if nums.index(num) >= start and (nums.index(num) + 1) <= len(nums):
    #             sum += num
    #     return sum

    # elif end and not start:
    #     for num in nums:
    #         if end <= len(nums):
    #             if nums.index(num) <= end:
    #                 sum += num
    #     return sum

    # elif start and end:
    #     for i in range(start, end + 1):
    #         sum += i
    #     return sum

    # elif nums:
    #     for num in nums:
    #         sum += num
    #     return sum



