def draw_stars(n):
  if n==1:
    return ['*']

  Stars=draw_stars(n//3)
  tmp=[]

  for i in Stars:
    tmp.append(i*3)
  for i in Stars:
    tmp.append(i+' '*(n//3)+i)
  for i in Stars:
    tmp.append(i*3)
    
  return tmp

N=int(input())
print('\n'.join(draw_stars(N)))