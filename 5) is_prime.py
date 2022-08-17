def is_prime(x):
  print(x)
  if x < 2:
    print(False)
    return False
  else:
    for n in range(2, x-1):
      if x % n == 0:
        print(False)
        return False
    print(True)
    return True