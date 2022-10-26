# Now it’s time to write some data to a new .txt file. We added the list comprehension from the first exercise to the code in the editor. Our goal in this exercise will be to write each element of that list to a file called output.txt. 
# The output.txt file that you write to will be created in your current folder - for simplicity, the folder has been hidden. output.txt will list each number on its own line. We can write to a Python file like so:

#       my_file.write("Data to be written")

# The .write() method takes a string argument, so we’ll need to do a few things here:
# You must close the file. You do this simply by calling my_file.close() (we did this for you in the last exercise). If you don’t close your file, Python won’t write to it properly. From here on out, you gotta close your files!
