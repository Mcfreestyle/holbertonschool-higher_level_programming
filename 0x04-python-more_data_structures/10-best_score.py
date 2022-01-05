#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    values = list(a_dictionary.values())
    max_score = values[0]
    for i in range(len(values) - 1):
        if max_score < values[i + 1]:
            max_score = values[i + 1]
    for k, v in a_dictionary.items():
        if v == max_score:
            return (k)
