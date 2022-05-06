def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    # create list comprehension
    # duplicates = [num for num in nums if nums.count(num) > 1 else return None]
    #  convert duplicates to set (to remove duplicates)
    # create for loop
    # for num in unique_duplicates 
    # if length of unique duplicates is >= 1
    # return num
    # else 
    # return None

    duplicates = [num for num in nums if nums.count(num) > 1]
    unique_duplicates = list(set(duplicates))

    for num in unique_duplicates:
        if len(unique_duplicates) >= 1:
            return num
        else:
            return None

