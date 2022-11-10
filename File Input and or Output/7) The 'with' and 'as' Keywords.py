# Programming is all about getting the computer to do the work. Is there a way to get Python to automatically close our files for us? Of course there is. This is Python. 
# You may not know this, but file objects contain a special pair of built-in methods: __enter__() and __exit__(). The details aren’t important, but what is important is that when a file object’s __exit__() method is invoked, it automatically closes the file. 
# How do we invoke this method? With with and as. The syntax looks like this:
        # with open("file", "mode") as variable:
        # # Read or write to the file
# 1. Check out the example in the editor. Note that we don’t explicitly close() our file, and remember that if we don’t close a file, our data will get stuck in the buffer. Click Run! Success! is written to a file called text.txt.
with open("text.txt", "w") as textfile:
  textfile.write("Success!")