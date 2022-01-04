#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_chr = None
    else:
        first_chr = sentence[0]
    new_tuple = (len(sentence), first_chr)
    return (new_tuple)
