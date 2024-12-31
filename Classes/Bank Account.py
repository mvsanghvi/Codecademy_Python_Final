class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print balance
  def deposit(self, amount):
    if amount <= 0:
      print "Some error message here"
    else:
      print amount
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount <= 0:
      print "Some error message here"
    else:
      print amount
      self.balance -= amount
      self.show_balance()
my_account = BankAccount("Your-name-here")
print my_account
