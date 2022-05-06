def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # create for loop
    # loop over each element
    # return: slice [-1:0]

    for letter in phrase:
        return phrase[-1::-1]
