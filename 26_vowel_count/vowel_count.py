def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # create vowels variable
    # create counter variable
    # lowercase phrase
    # create for loop
    # loop over letter in phrase
    # if letter in vowels
    # if letter in counter
    #  counter[letter] += 1
    # else
    #  counter[letter] = 1
    # return counter

    vowels = 'aeiuo'
    counter = {}
    new_phrase = phrase.lower()

    for letter in new_phrase:
        if letter in vowels:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
    return counter




