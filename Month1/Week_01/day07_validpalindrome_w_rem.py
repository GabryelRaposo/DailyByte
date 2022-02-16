"""
This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
Ex: Given the following strings...
    "abcba", return true
    "foobof", return true (remove the first 'o', the second 'o', or 'b')
    "abccab", return false
"""

def palindrome_string(str1):
    pre = list(str1)
    k = str1[::-1]
    if (k == str1):
        return True  
    else:
        for char in str1:
            pre.remove(char)
            new_palindrome = pre[::-1]
            if (new_palindrome == pre):
                return True 
            else:
                pre = list(str1)
        return False


print(palindrome_string("abcba"))
print(palindrome_string("foobof"))
print(palindrome_string('abccab'))



