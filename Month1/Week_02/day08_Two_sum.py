"""Given an array of integers, return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)"""

def two_sum(array, k):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                value = array[i]+array[j]
                if value == k:
                    return True
    
    if value != k:
        return False

assert two_sum([1, 3, 8, 2], 10) == True
assert two_sum([3, 9, 13, 7], 8) == False
assert two_sum([4, 2, 6, 5, 2], 4) == True
