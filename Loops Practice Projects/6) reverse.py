def reverse(text):
  print(text)
  rev=""
  for i in text:
    rev= i+rev
  print(rev)
  return rev

#Alternative method
# def reverse(text):
#   print(text)
#   t_len=len(text)-1
#   rev=""
#   while t_len >= 0:
#     rev= rev + text[t_len]
#     t_len -= 1
#   print(rev)
#   return rev  

