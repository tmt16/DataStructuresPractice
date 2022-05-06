from itertools import count


def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    # create count variable
    # create for loop
    # loop over word
    # if letter = index of word
    # increase count +1
    # return count

    count = 0
    i = 0

    for element in word:
        if letter.lower() == element[i].lower():
            count += 1
    return count
