# Here’s a simple example of list comprehension syntax:
#         new_list = [x for x in range(1, 6)]
#         # => [1, 2, 3, 4, 5]

# This will create a new_list populated by the numbers one to five. If you want those numbers doubled, you could use:
#         doubles = [x * 2 for x in range(1, 6)]
#         # => [2, 4, 6, 8, 10]

# And if you only wanted the doubled numbers that are evenly divisible by three:
#         doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
#         # => [6]

# 1. Use a list comprehension to build a list called even_squares in the editor. 
#     Your even_squares list should include the squares of the even numbers between 1 to 11. Your list should start [4, 16, 36...] and go from there.

even_squares = [x ** 2 for x in range(1, 12) if x  % 2 == 0]

print(even_squares)
