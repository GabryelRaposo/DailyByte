def vacuum_cleaner(str):
    u = d = l =r = 0
    k = list(str)
    for i in k:
      if (i == 'u'):
        u = u+1
      if (i == 'd'):
        d = d+1 
      if (i == 'l'):
        l = l+1
      if (i == 'r'):
        r = r+1
    if u == d and r == l:
        return 1


vacuum_cleaner('RUULLDRD')
