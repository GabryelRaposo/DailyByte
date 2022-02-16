''' Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each 
sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]'''

def Uncommon_words(str1,str2):
    str1 = list(set(str1.split()))
    str2 = list(set(str2.split()))

    output = []
    for i in range(len(str1)):
        k = 0
        for j in range(len(str2)):
            if str1[i] != str2[j]:
                k = k+1
            if k == len(str2):
                output.append(str1[i])

    for i in range(len(str2)):
        k = 0
        for j in range(len(str1)):
            if str2[i] != str1[j]:
                k = k+1
            if k == len(str1):
                output.append(str2[i])
    return output

print(Uncommon_words('the quick', 'brown fox'))
print(Uncommon_words('the tortoise beat the haire', 'the tortoise lost to the haire'))
print(Uncommon_words('copper coffee pot', 'hot coffee pot'))