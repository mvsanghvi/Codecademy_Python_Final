# Classes can be very useful for storing complicated objects with their own methods and variables. Defining a class is much like defining a function, but we use the class keyword instead. 
# We also use the word object in parentheses because we want our classes to inherit the object class. This means that our class has all the properties of an object, which is the simplest, most basic class. 
# Later we’ll see that classes can inherit other, more complicated classes. An empty class would look like this:

        # class ClassName(object):
        #   # class statements go here

# 1. Define a new class named “Car”. For now, since we have to put something inside the class, use the pass keyword.
class Car(object):
  pass

# We can use classes to create new objects, which we say are instances of those classes.
# Creating a new instance of a class is as easy as saying:

        # newObject = ClassName()
# 2. Below your Car class, create a new object named my_car that is an instance of Car.
class Car(object):
  pass

my_car= Car()


