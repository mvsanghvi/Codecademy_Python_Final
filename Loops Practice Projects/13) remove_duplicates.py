#Using only commands and data storage collections taught in Codecademy
def remove_duplicates(lst):
  print(lst)
  new_sequence= []
  for i in lst:
    if i not in new_sequence:
      new_sequence.append(i)
    else:
      continue
  print(new_sequence)
  return new_sequence

#Using sets, which not covered in Codecademy lessons
# def remove_duplicates(lst):
#   print(lst)
#   freq= {}
#   for x in lst:
#     print(x)
#     if (x in freq):
#       freq[x] += 1
#       print(freq[x])
#     else:
#       freq[x] = 1
#     print(freq)
#   return list(freq.keys())