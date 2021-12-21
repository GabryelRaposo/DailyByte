def palindrome_string(str1):
    k = str1[::-1]
    if (k == str1):
        return True
    else:
        return False
string = 'level'

palindrome_string(string)