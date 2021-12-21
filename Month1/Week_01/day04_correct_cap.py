def correct_capitalization(str):
    lower = 0
    if str.isupper() or str.islower():
      return True
    k = list(str)
    xlen = len(k)
    if k[0].isupper():
      for i in range(xlen-1):
        if k[i+1].islower():
          lower = lower +1
      if lower == xlen-1:
        return True
      else:
        return False
    else: 
        return False

assert correct_capitalization("USA") == True
assert correct_capitalization("Calvin") == True
assert correct_capitalization('compUter') == False
assert correct_capitalization('coding') == True

print('The soluction is correct')