def count(sequence, item):
  print(sequence, ", ", item)
  sum= 0
  for i in sequence:
    if i== item:
      sum += 1
  print(sum)
  return sum