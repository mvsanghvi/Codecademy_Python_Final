#We can modify variables that belong to a class the same way that we initialize those member variables. This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.
# 1. Inside the Car class, add a method drive_car that sets self.condition to the string "used". Remove the call to my_car.display_car() and instead print only the condition of your car. Then drive your car by calling the drive_car method.
# Finally, print the condition of your car again to see how its value changes.

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
    
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

# One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from their parent classes. 
# This saves us time and helps us build more complicated objects, since these child classes can also include additional variables or methods. We define a “child” class that inherits all of the variables and functions from its “parent” class like so:
        # class ChildClass(ParentClass):
        #   # new variables and functions go here
# Normally we use object as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.

# 1. Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes a battery_type member variable in addition to the model, color and mpg. Then, create an electric car named my_car with a "molten salt" battery_type. 
# Supply values of your choice for the other three inputs (model, color and mpg).
