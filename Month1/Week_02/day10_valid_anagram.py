'''Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false'''

def valid_anagram(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    str1.sort()
    str2.sort()
    k=0
    for i,j in zip(str1,str2):
      if i == j:
        k = k+1
    if k == len(str1):
        return True       
    else:
        return False

assert valid_anagram('cat', 'tac') == True
assert valid_anagram('caa', 'aac') == True
assert valid_anagram('listen','silent') == True
assert valid_anagram('program','function') == False

print("everything alright")