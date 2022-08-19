# Let’s start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

# d = {
#   "Name": "Guido",
#   "Age": 56,
#   "BDFL": True
# }
# print d.items()
# # => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]

# Note that the .items() method doesn’t return key/value pairs in any specific order.

# 1. Create your own Python dictionary, my_dict, in the editor to the right with two or three key/value pairs.
#     Then, print the result of calling the my_dict.items().

my_dict = {
  "Name": "Megan",
  "Age": 25,
  "Brown Eyes": True
}
print(my_dict.items())