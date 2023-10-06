#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if (my_list is None or len(my_list) == 0):
        return
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
