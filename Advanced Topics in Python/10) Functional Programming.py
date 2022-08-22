# One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you’re allowed to pass functions around just as if they were variables or values. 
# Sometimes we take this for granted, but not all languages allow this!
# Check out the code at the right. See the lambda bit? Typing: 
#     lambda x: x % 3 == 0

# Is the same as:

#     def by_three(x):
#         return x % 3 == 0

# Only we don’t need to actually give the function a name; it does its work and returns a value without one. That’s why the function the lambda creates is an anonymous function.
# When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter() so that lambda should ensure only "Python" is returned
print(filter(lambda i: i=="Python", languages))

# All right! Time to test out filter() and lambda expressions:

#     cubes = [x ** 3 for x in range(1, 11)]
#     filter(lambda x: x % 3 == 0, cubes)

# The example above is just a reminder of the syntax.
# Instructions
# 1. Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here! Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).

squares= [x ** 2 for x in range(1,11)]
print(filter(lambda x: x>=30 and x<=70, squares))

# 2. Create a new variable called message. Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.
# Finally, print your message to the console.

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message= filter(lambda x: x!="X", garbled)
print(message)
