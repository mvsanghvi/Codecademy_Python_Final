"""
This will
act as an interactive
calendar
"""
from time import sleep, strftime
USER_FIRST_NAME = "Gilberto"
calendar = {}
def welcome():
  print("Welcome, " + USER_FIRST_NAME + ".")
  print("Calendar starting...")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y")) 
  print("The current time is: " + strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V': 
      if len(calendar.keys()) < 1:
        print("Calendar empty.")
      else:
        print(calendar)
    elif user_choice == 'U':
        date = raw_input("What date? ")
        update = raw_input("Enter the update: ")
        calendar[date] = update
        print("Update was successful")
        print(calendar)
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("Invalid date entered.")
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
          calendar[date] = event
          print("Event addition was successful")
          print(calendar)
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print("Calendar empty.") 
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print("Deletion was successful")
          else:
            print("Incorrect event specified")
    elif user_choice == 'X':
      print("Exiting program...")
      quit()
start_calendar()
