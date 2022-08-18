def purify(lst):
  print(lst)
  no_odd=[]
  for i in lst:
    if i%2==0:
      no_odd.append(i)
    else:
      continue
  print(no_odd)
  return no_odd