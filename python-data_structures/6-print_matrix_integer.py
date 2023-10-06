#!/usr/bin/python3
# 6-print_matrix_integer.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for fila in matrix:
        for i in fila:
            print("{:d}".format(i), end=" ")
        print()
    if not matrix:
        print()
