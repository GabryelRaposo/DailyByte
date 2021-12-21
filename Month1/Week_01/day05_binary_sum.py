"""
This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0
Ex: Given the following binary strings...
    "100" + "1", return "101"
    "11" + "1", return "100"
    "1" + "0", return  "1"
"""

#this code isn't completely right, there are certain issues to be hulled
def sum_digits(a,b,carry="0"):
    if a and b == "1":
        return ("1","0") if carry == "0" else ("1","1")
    elif a == "0" and b == "1" or a == "1" and b == "0":
        return ("0","1") if carry == "0" else("1","0")
    return ("0", "0") if carry=="0" else ("0", "1")

def sum_binary(n1,n2):
  max_len = max(len(n1), len(n2))
  n1 = n1.zfill(max_len)
  n2 = n2.zfill(max_len)
  n1 = list(n1)
  n2 = list(n2)
  print(n1)
  print(n2)
  carry = 0
  r = ''

  for i in range(len(n1) -1, -1,-1):
    print(n1[i])
    print(n2[i])
    print(carry)
    k = sum_digits('n1[i]', 'n2[i]', 'carry')
    print(k)
    carry = k[0]
    print('new carry', carry)
    r = r + k[1]

  return r  
    
print(sum_binary('11', '1'))