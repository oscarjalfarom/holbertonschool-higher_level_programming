#!/usr/bin/python3
# 8-multiple_returns.py
# Oscar J Alfaro M <5826@holbertonschool.com>
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if (sentence_length > 0):
        first_char = sentence[0]
    else:
        first_char = "None"
    new_tuple = (sentence_length, first_char)
    return (new_tuple)
