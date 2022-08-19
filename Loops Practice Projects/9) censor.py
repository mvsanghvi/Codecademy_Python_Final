def censor(text, word):
  print(word)
  censored = '*' * len(word)
  print(censored)
  censored_text = text.replace(word, censored)
  print(censored_text)
  return censored_text