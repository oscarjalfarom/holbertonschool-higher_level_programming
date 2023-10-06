#!/usr/bin/python3
# 4-new_in_list.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def new_in_list(my_list, idx, element):
    """replace an element in a list at a specific position without modifying the original list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list[:])
    cp_my_list = my_list[:]
    cp_my_list[idx] = element
    return (cp_my_list)
