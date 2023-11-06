#!/usr/bin/python3
# 0-read_file.py
# Oscar J Alfaro M <5826@holbertonschool.com>

"""
Module that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function that reads a text file and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        for lines in file:
            print(lines, end='')
