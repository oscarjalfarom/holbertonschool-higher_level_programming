#!/usr/bin/python3
# 11-delete_at.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def delete_at(my_list=[], idx=0):
    if (idx < 0):
        return (my_list)
    elif (idx >= len(my_list)):
        return (my_list)
    else:
        del my_list[idx]
        return (my_list)
