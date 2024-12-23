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
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

# Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own drive_car() method that has different functionality than the original Car class’s.
# 1. Inside ElectricCar add a new method drive_car that changes the car’s condition to the string "like new". Then, outside of ElectricCar, print the condition of my_car. Next, drive my_car by calling the drive_car function. Finally, print the condition of my_car again
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
  def drive_car(self):
    self.condition= "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

# Chances are, you won’t be designing Car classes in the real world anytime soon. Usually, classes are most useful for holding and accessing abstract collections of data.
# One useful class method to override is the built-in __repr__() method, which is short for representation; by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a print statement).
# 1. Define a Point3D class that inherits from object. Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x, self.y, self.z
# Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the following format: (x, y, z). 
# Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.
class Point3D(object):
  def __init__(self, x, y, z):
    self.x= x
    self.y= y
    self.z= z
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point= Point3D(1, 2, 3)
print(my_point)