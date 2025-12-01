from itertools import pairwise

def sorted_is(a, key=lambda x: x):
    if len(a) <= 1: 
        return True 
    for current, next_item in pairwise(a):
        if key(current) > key(next_item):
            return False 
    return True
