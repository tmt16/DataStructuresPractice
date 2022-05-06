from itertools import zip_longest
from operator import index


def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    # create dict variable
    # create for loop
    # for index and val in enumerate function of keys
    #  val of dict = index of values
    #  if index <len(values)
    #  else None
    # return dict

    dict = {}

    for index, val in enumerate(keys):
        dict[val] = values[index] if index < len(values) else None

    return dict

    


