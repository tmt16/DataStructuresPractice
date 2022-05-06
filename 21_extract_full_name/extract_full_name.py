def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    # create list_of_values variable
    # create for loop
    # loop over names in people
    # create first_name variable
    # create last_name variable
    # append first_name and last_name to list_values with space in between
    # return list_of_values

    list_of_values = []

    for names in people:
        first_name = names['first']
        last_name = names['last']
        list_of_values.append(first_name + ' ' + last_name)
    return list_of_values

