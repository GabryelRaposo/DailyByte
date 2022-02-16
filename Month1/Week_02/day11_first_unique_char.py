'''Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0'''

def first_unique_char(str1):
    str1=list(str1)
    value = len(str1) - 1
    for i in range(len(str1)):
        k=0
        #print('valor i', str1[i])
        for j in range(len(str1)):
            if i != j and str1[i] != str1[j]: 
                #print('valor j', str1[j])
                k = k+1
            if k == value:
                return i

    return -1      

print(first_unique_char('abcabd'))
print(first_unique_char('thedailybyte'))
print(first_unique_char('developer'))
print(first_unique_char('ddeevv'))


