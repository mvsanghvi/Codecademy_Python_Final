# A basic class consists only of the class keyword, the name of the class, and the class from which the new class inherits in parentheses. (We’ll get to inheritance soon.) For now, our classes will inherit from the object class, like so:

        # class NewClass(object):
        #   # Class magic here

# This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.

# We’d like our classes to do more than… well, nothing, so we’ll have to replace our pass with something else.
# You may have noticed in our example back in the first exercise that we started our class definition off with an odd-looking function: __init__(). 
# This function is required for classes, and it’s used to initialize the objects it creates. __init__() always takes at least one argument, self, that refers to the object being created. 
# You can think of __init__() as the function that “boots up” each object the class creates.

class Animal(object):
  def __init__(self):
    pass 

# Excellent! Let’s make one more tweak to our class definition, then go ahead and instantiate (create) our first object.
# So far, __init__() only takes one parameter: self. This is a Python convention; there’s nothing magic about the word self. 
# However, it’s overwhelmingly common to use self as the first parameter in __init__(), so you should do this so that other people will understand your code.
# The part that is magic is the fact that self is the first parameter passed to __init__(). 
# Python will use the first parameter that __init__() receives to refer to the object being created; this is why it’s often called self, since this parameter gives the object being created its identity.

class Animal(object):
  def __init__(self, name):
    self.name= name 