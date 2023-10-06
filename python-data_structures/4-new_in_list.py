#!/usr/bin/python3
# 4-new_in_list.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list[:])
    cp_my_list = my_list[:]
    cp_my_list[idx] = element
    return (cp_my_list)
