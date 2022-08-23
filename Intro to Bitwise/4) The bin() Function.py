# There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation of that integer in a string. 
# (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)

# You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. (We won’t be dealing with those here, however.)

print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)


# Python has an int() function that you’ve seen a bit of already. It can turn non-integer input into an integer, like this:

#         int("42")
#         # ==> 42

# What you might not know is that the int function actually has an optional second parameter.

#         int("110", 2)
#         # ==> 6

# When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)