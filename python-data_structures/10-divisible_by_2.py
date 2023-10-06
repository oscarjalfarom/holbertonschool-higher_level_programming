#!/usr/bin/python3
# 10-divisible_by_2.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def divisible_by_2(my_list=[]):
    results = []
    if (len(my_list) > 0):
        for i in range(0, len(my_list)):
            if (my_list[i] % 2 == 0):
                results.append(True)
            else:
                results.append(False)
    return (results)
