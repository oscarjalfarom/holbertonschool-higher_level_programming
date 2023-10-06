#!/usr/bin/python3
# 5-no_c.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_str = ""
    for i in range(0, len(my_string)):
        if (my_string[i] not in ('c', 'C')):
            new_str += my_string[i]
    return (new_str)
