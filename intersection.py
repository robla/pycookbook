#!/usr/bin/env python3
# This script was created with Google Bard after a few prompts
# on 2023-09-25 by robla

def intersection(array1, array2):
    """Returns the intersection of two arrays of strings."""
    set1 = set(array1)
    set2 = set(array2)

    intersection = set1.intersection(set2)

    return list(intersection)


array1 = ["dog", "cat", "cow"]
array2 = ["cat", "cow", "cougar"]

intersection = intersection(array1, array2)

print(intersection)
