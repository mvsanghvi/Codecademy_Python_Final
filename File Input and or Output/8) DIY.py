# It worked! Our Python program successfully wrote to text.txt.
# 1. Now you try: write any data you like to a file called text.txt using with…as. Give your file object the usual name: my_file.
with open("text.txt", "w") as my_file:
  my_file.write("Done.")