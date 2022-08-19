# Let’s say you wanted to build a list of the numbers from 0 to 50 (inclusive). We could do this pretty easily:

#         my_list = range(51)

# But what if we wanted to generate a list according to some logic—for example, a list of all the even numbers from 0 to 50?

# Python’s answer to this is the list comprehension. List comprehensions are a powerful way to generate lists using the for/in and if keywords we’ve learned.

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)