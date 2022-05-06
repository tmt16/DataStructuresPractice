from ast import Num


def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'  
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    # create new_list variable
    # create new_length variable
    # create for loop
    # loop over char in phrase
    # if n < 3
    #  return 'Truncation must be at least 3 characters.'
    # if len(phrase) < n
    #  return phrase
    # if len(phrase) >= n
    #  new_phrase += char
    # if new_phrase = n
    # new_length = new_list -3
    #  return string of (new_phrase) + "..."

    new_list = []
    new_length = []

    for char in phrase:
        if n < 3:
            return 'Truncation must be at least 3 characters.'
        if len(phrase) < n:
            return phrase
        if len(phrase) >= n:
            new_list += char
        if len(new_list) == n:
            new_length = new_list[:len(new_list) - 3]
    return (''.join(new_length)+'...')
