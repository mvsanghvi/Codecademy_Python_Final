"""
This will
calculate the area
of either a circle or traingle!
"""
print("The calculator is running")
option = raw_input("What shape are you calculating? Endter C for Cirle or T for Triangle: ")
if option == 'C':
  radius = float(raw_input("Enter radius: "))
  areac= 3.14159*radius**2
  print("Area = % f" % areac)
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  areat= 0.5*base*height
  print("Area = % f" % areat)
else:
  print("Invalid shape enterred")
print("Exiting program. Goodbye :)")