'''Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0'''

def jewels_stones(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    k=0
    for i in str1:
        for j in str2:
            if i == j:
                k = k+1
    return k
print(jewels_stones('abc','ac'))  
print(jewels_stones('Af','AaaddfFf'))  
print(jewels_stones('AYOPD','ayopd'))