#!/usr/bin/python3
# 6-print_matrix_integer.py
# Oscar J Alfaro M <5826@holbertonschool.com>

def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print("")
        return
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (j < len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]))
