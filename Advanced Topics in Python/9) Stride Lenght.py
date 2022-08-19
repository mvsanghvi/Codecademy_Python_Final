# A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.
# Further, a stride length of 1 traverses the list “by ones,” a stride length of 2 traverses the list “by twos,” and so on.

# 1. Create a variable, backwards_by_tens, and set it equal to the result of going backwards through to_one_hundred by tens. Go ahead and print backwards_by_tens to the console.

to_one_hundred = range(101)
# Add your code below!
backwards_by_tens=to_one_hundred[::-10]
print(backwards_by_tens)

# 2. Create a list, to_21, that’s just the numbers from 1 to 21, inclusive.
#     Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
#     Finally, create a third list, middle_third, that’s equal to the middle third of to_21, from 8 to 14, inclusive.
to_21= range(1,22)
odds= to_21[::2]
print(odds)
middle_third=to_21[7:14]
print(middle_third)