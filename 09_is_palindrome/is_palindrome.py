from re import I


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # new_phrase variable to remove spaces
    # create variable: reversed_list[::-1]
    #  if new_phrase == reversed_list
    #  return True
    # else: return False
    
    new_phrase = phrase.lower().replace(" ", "")
    reversed_list = new_phrase[::-1]

    if new_phrase == reversed_list:
        return True
    else:
        return False
