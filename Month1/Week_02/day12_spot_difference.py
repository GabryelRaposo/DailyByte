'''You are given two strings, s and t which only consist of lowercase letters. t is generated by shuffling the letters in s as well as potentially adding an additional random character. Return the letter that was randomly added to t if it exists, otherwise, return ’  ‘.
Note: You may assume that at most one additional character can be added to t.

Ex: Given the following strings...

s = "foobar", t = "barfoot", return 't'
s = "ide", t = "idea", return 'a'
s = "coding", t "ingcod", return '' 
'''

def spot_the_difference(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    str1.sort()
    str2.sort()
    k=0
    for i,j in zip(str2,str1):
        if i == j:
            k = k+1
        if i != j:
            extra_character = i
            return extra_character
    if k == len(str2):
        return "''"
    else:
        return str2[-1]

print(spot_the_difference('foobar', 'barfoot'))
print(spot_the_difference('ide', 'idea'))
print(spot_the_difference('coding', 'ingcod'))
