# Inheritance is a tricky concept, so let’s go through it step by step.
# Inheritance is the process by which one class takes on the attributes and methods of another, and it’s used to express an is-a relationship. 
# For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn’t inherit from the Tractor class (even if they have a lot of attributes and methods in common). 
# Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.

# 1. Check out the code in the editor. We’ve defined a class, Customer, as well as a ReturningCustomer class that inherits from Customer. 
# Note that we don’t define the display_cart method in the body of ReturningCustomer, but it will still have access to that method via inheritance.


class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

# In Python, inheritance works like this:
    # class DerivedClass(BaseClass):
    #   # code goes here
# where DerivedClass is the new class you’re making and BaseClass is the class from which that new class inherits.

# 1. On lines 1-4, we’ve created a class named Shape.
#   Create your own class, Triangle, that inherits from Shape. Inside the Triangle class, write an __init__() function that takes four arguments: self, side1, side2, and side3.
#   Inside the __init__() function, set self.side1 = side1, self.side2 = side2, and self.side3 = side3.

class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3