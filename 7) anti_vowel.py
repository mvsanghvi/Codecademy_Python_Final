def anti_vowel(text):
  print(text)
  no_vowel=""
  vowels= "AaEeIiOoUu"
  for i in text:
    if i in vowels:
      continue
    else:
      no_vowel= no_vowel+i
  print(no_vowel)
  return no_vowel