def factorial(x):
  print(x)
  total_fac=1
  for i in range(1,x+1):
    total_fac*=i
    i-=1
  print(total_fac)
  return total_fac