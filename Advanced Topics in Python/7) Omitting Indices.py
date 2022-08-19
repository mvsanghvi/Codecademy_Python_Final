# Sometimes we only want part of a Python list. Maybe we only want the first few elements; maybe we only want the last few. Maybe we want every other element!
# List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

#         [start:end:stride]

# Where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride describes the space between items in the sliced list. For example, a stride of 2 would select every other item from the original list to place in the sliced list.

# If you don’t pass a particular index to the list slice, Python will pick a default.

#         to_five = ['A', 'B', 'C', 'D', 'E']
        
#         print to_five[3:]
#         # prints ['D', 'E'] 
        
#         print to_five[:2]
#         # prints ['A', 'B']
        
#         print to_five[::2]
#         # print ['A', 'C', 'E']

# 1. The default starting index is 0.
# 2. The default ending index is the end of the list.
# 3. The default stride is 1.

# Use list slicing to print out every odd element of my_list from start to finish. Omit the start and end index. You only need to specify a stride.

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print(my_list[::2])