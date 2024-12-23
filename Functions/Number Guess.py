"""
This is a game
that compares user guesses
to dice rolls
"""
from random import randint
from time import sleep
def get_user_guess():
  guess= int(raw_input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print("Max possible value is %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("Number guess is too large. Try again")
  else:
    print("Rolling...")
    sleep(2)
    print("The 1st roll is: %d") % first_roll
    sleep(1)
    print("The 2nd roll is: %d") % second_roll
    sleep (1)
    total_roll= first_roll+second_roll
    print("The total values is: %d") % total_roll
    print("Result...")
    sleep (1)
    if total_roll == guess:
      print("Congrats! You won!")
    else:
      print("You lost, better luck next time :(")
roll_dice(6)