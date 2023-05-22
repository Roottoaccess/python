# Here we will see about file handling in python
# suppose we have a string
s = "Biswarup is a good boy"

# Using the context manager, it helps to run the code without closing it
# Creating a file (text.txt) and writing some text init
with open("text.txt", "w") as f:
    f.write(s)

# Now we will do the operations in reading a file
with open("text.txt", "r") as f:
    s = f.read()
    print(s)

# Appendiing the file
with open("text.txt", "a") as f:
    f.write("This is great summer")