# Sometimes you’ll want one class that inherits from another to not only take on the methods and attributes of its parent, but to override one or more of them.
        # class Employee(object):
        #   def __init__(self, name):
        #     self.name = name
        #   def greet(self, other):
        #     print "Hello, %s" % other.name
        
        # class CEO(Employee):
        #   def greet(self, other):
        #     print "Get back to work, %s!" % other.name
        
        # ceo = CEO("Emily")
        # emp = Employee("Steve")
        # emp.greet(ceo)
        # # Hello, Emily
        # ceo.greet(emp)
        # # Get back to work, Steve!
# Rather than have a separate greet_underling method for our CEO, we override (or re-create) the greet method on top of the base Employee.greet method. This way, we don’t need to know what type of Employee we have before we greet another Employee.

# 1. Create a new class, PartTimeEmployee, that inherits from Employee.
# Give your derived class a calculate_wage method that overrides Employee‘s. It should take self and hours as arguments.
# Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.
# It should return the part-time employee’s number of hours worked multiplied by 12.00 (that is, they get $12.00 per hour instead of $20.00).

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

# On the flip side, sometimes you’ll be working with a derived class (or subclass) and realize that you’ve overwritten a method or attribute defined in that class’ base class (also called a parent or superclass) that you actually need. Have no fear! 
# You can directly access the attributes or methods of a superclass with Python’s built-in super call. The syntax looks like this:
    # class Derived(Base):
    #   def m(self):
    #     return super(Derived, self).m()
# Where m() is a method from the base class.
# 1. First, inside your PartTimeEmployee class:
#     Add a new method called full_time_wage with the arguments self and hours.
#     That method should return the result of a super call to the calculate_wage method of PartTimeEmployee‘s parent class. Use the example above for help.
#   Then, after your class:
#     Create an instance of the PartTimeEmployee class called milton. Don’t forget to give it a name.
#     Finally, print out the result of calling his full_time_wage method. You should see his wage printed out at $20.00 per hour! (That is, for 10 hours, the result should be 200.00.)
# You super call should look something like this:
    # def full_time_wage(self, hours):
    #   return super(PartTimeEmployee, self).method(args)
# Where method is the method you want (calculate_wage) and args are the arguments that method takes.


class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton= PartTimeEmployee("milton")
print(milton.full_time_wage(10))
