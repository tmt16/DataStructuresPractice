def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # create new_list variable

    # create for loop
    # loop over each letter in phrase
    # if to_swap.lower() == letter.lower()
    #  append letter to new_list with swapcase()
    # if to_swap.lower() != letter.lower()
    # append letter to new_list
    # return new_list as string with no spaces

    new_str = ""

    for letter in phrase:
        if to_swap.lower() == letter.lower():
            new_str += letter.swapcase()

        if to_swap.lower() != letter.lower():
            new_str += letter

    return "".join(new_str)


