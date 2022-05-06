from ast import Num
import string


def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    # if isinstance of num a string or if num < 0
    #  return None
    # if isinstance of num an integer
    # return phrase * num

    if isinstance(num, str) or num < 0:
        return None

    if isinstance(num, int):
        return phrase * num


