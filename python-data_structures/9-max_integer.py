#!/usr/bin/python3
# 9-max_integer.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def max_integer(my_list=[]):
    if (len(my_list) <= 0):
        return ("None")
    else:
        max_num = my_list[0]
        for i in range(1, len(my_list)):
            if (my_list[i] > max_num):
                max_num = my_list[i]
        return (max_num)
