def vacuum_cleaner(str):
    U = D = L = R = 0
    k = list(str)
    for i in k:
      if (i == 'U'):
        U = U+1
      if (i == 'D'):
        D = D+1 
      if (i == 'L'):
        L = L+1
      if (i == 'R'):
        R = R+1
    if U == D and R == L:
      return True
    else: 
      return False  

assert vacuum_cleaner("LR") == True
assert vacuum_cleaner("URURD") == False
assert vacuum_cleaner('RUULLDRD') == True

print('The soluction is correct')