# There is a special function named __init__() that gets called whenever we create a new instance of a class. It exists by default, even though we don’t see it. 
# However, we can define our own __init__() function inside the class, overwriting the default version. We might want to do this in order to provide more input variables, just like we would with any other function.
# The first argument passed to __init__() must always be the keyword self - this is how the object keeps track of itself internally - but we can pass additional variables after that.
# In order to assign a variable to the class (creating a member variable), we use dot notation. For instance, if we passed newVariable into our class, inside the __init__() function we would say:

        # self.new_variable = new_variable

# 1. Define the __init__() function of the Car class to take four inputs: self, model, color, and mpg. Assign the last three inputs to member variables of the same name by using the self keyword.
# Then, modify the object my_car to provide the following inputs at initialization:

        # model = "DeLorean"
        # color = "silver"
        # mpg = 88

# You don’t need to include the self keyword when you create an instance of a class, because self gets added to the beginning of your list of inputs automatically by the class definition.

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

my_car= Car("DeLorean", "silver", 88)

# Calling class member variables works the same whether those values are created within the class (like our car’s condition) or values are passed into the new object at initialization. 
# We use dot notation to access the member variables of classes since those variables belong to the object.
# For instance, if we had created a member variable named new_variable, a new instance of the class named new_object could access this variable by saying:

        # new_object.new_variable

# 2. Now that you’ve created my_car print its member variables:
#     First print the model of my_car. Click “Stuck? Get a hint!” for an example.
#     Then print out the color of my_car.
#     Then print out the mpg of my_car.
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

my_car= Car("DeLorean", "silver", 88)
print(my_car.model)
print(my_car.color)
print(my_car.mpg)

# Besides member variables, classes can also have their own methods. For example:

# class Square(object):
#   def __init__(self, side):
#     self.side = side
 
#   def perimeter(self):
#     return self.side * 4

# The perimeter() class method is identical to defining any other function, except that it is written inside of the Square class definition.
# Just like when we defined __init__(), you need to provide self as the first argument of any class method.
# 1. Inside the Car class, add a method named display_car to Car that will reference the Car’s member variables to return the string, "This is a [color] [model] with [mpg] MPG." You can use the str() function to turn your mpg into a string when creating the display string.
# Replace the individual print statements with a single print command that displays the result of calling my_car.display_car()

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))

my_car = Car("DeLorean", "silver", 88)
print(my_car.display_car())