# Until now, the Python code you’ve been writing comes from one source and only goes to one place: you type it in at the keyboard and its results are displayed in the console. 
# But what if you want to read information from a file on your computer, and/or write that information to another file? This process is called file I/O (the “I/O” stands for “input/output”), and Python has a number of built-in functions that handle this for you.
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()
