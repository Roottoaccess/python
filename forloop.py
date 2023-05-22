# Here we will look about for loop in python
# for i in range(5):
#     print(i + 1)

# We can apply for loop with a list also
# for loop can be perform in sets also
a = [12,  42, 62, 88]
b = {14, 25, 62, 32, 12}
for item in b:
    print(item)

# Making a table generator of any number using for loop
user = int(input("Enter any number to find the table of : "))
# Computing the table part
for i in range(1, 11):
    result = user * i
    print(user, "X", i, "=", result)
