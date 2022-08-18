def remove_duplicates(lst):
  print(lst)
  freq= {}
  for x in lst:
    print(x)
    if (x in freq):
      freq[x] += 1
      #print x
      print(freq[x])
      # if freq[x] > 1:
        # lst.remove(x)
        # print lst
    else:
      freq[x] = 1
    print(freq)
  return list(freq.keys())