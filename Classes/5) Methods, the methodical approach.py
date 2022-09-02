# When a class has its own functions, those functions are called methods. You’ve already seen one such method: __init__(). But you can also define your own methods!

# 1. Add a method, description, to your Animal class. Using two separate print statements, it should print out the name and age of the animal it’s called on. 
# Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
hippo = Animal("Bobo", 6)

# A class can have any number of member variables. These are variables that are available to all members of a class.

        # hippo = Animal("Jake", 12)
        # cat = Animal("Boots", 3)
        # print hippo.is_alive
        # hippo.is_alive = False
        # print hippo.is_alive
        # print cat.is_alive

#     In the example above, we create two instances of an Animal.
#     Then we print out True, the default value stored in hippo’s is_alive member variable.
#     Next, we set that to False and print it out to make sure.
#     Finally, we print out True, the value stored in cat’s is_alive member variable. We only changed the variable in hippo, not in cat.

# Let’s add another member variable to Animal. After line 3, add a second member variable called health that contains the string "good".
# Then, create two new Animals: sloth and ocelot. (Give them whatever names and ages you like.)
# Finally, on three separate lines, print out the health of your hippo, sloth, and ocelot.

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health= "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

hippo = Animal("Bobo", 6)
sloth = Animal("Slow", 10)
ocelot= Animal("Lottie", 1)

print(hippo.health)
print(sloth.health)
print(ocelot.health)

