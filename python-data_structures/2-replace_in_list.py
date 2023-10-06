#!/usr/bin/python3
# 2-replace_in_list.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def replace_in_list(my_list, idx, element):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    my_list[idx] = element
    return (my_list)
