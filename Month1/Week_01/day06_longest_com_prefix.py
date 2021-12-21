"""
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.
Ex: Given the following arrays...
    ["colorado", "color", "cold"], return "col"
    ["a", "b", "c"], return ""
    ["spot", "spotty", "spotted"], return "spot"
"""


def longest_prefix(array):
    new_result = array[0]
    lenx = len(array)
    
    for i in range(1, lenx):
        string = new_result
        new_result = ""
        for char1,char2 in zip(string, array[i]):
            if char1 == char2:
                new_result = new_result + char1
            else:
                break
                
    if new_result == "":      #adjusting the return in case of no coincidence in the characters
      new_result = '\"\"'

    return new_result

print(longest_prefix(["colorado", "color", "cold"]))
print(longest_prefix(["a", "b", "c"]))
print(longest_prefix(["spot", "spotty", "spotted"]))

        