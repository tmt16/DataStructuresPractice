from calendar import SUNDAY


def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

    # create day object
    # loop over object 
    # if day_of_week matches the key in day
    # return value 
    # else
    # return None

    week_day = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    for (num, day) in week_day.items():
        if day_of_week == num:
            return day
