def median(into):
  print(into)
  into.sort()
  ind1=0
  ind2=0
  total=0
  mid= 0
  print("Sorted", into)
  for i in range(0, len(into)):
    if len(into)%2==0:
      ind1=(len(into)/2)-1
      ind2=len(into)/2
      total= into[int(ind1)]+into[int(ind2)]
      mid= total/2.0
    else:
      ind1=len(into)/2
      mid= into[int(ind1)]
  print(mid)
  return mid