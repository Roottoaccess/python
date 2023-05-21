# Here we will learn about the list programs and to use the methods
# Building a list
# List is mutable but Strings are unmutable
li = [2, 4, 8, 12, 14, 18, 18, 14, "Jeet"]

# Printing the type
print(type(li))

# Printing the list
print(li)

# Methods we can use in list if we want to remove an element from the list we will do
li.remove("Jeet")
print(li)

# To count an element we need to do that
print("Counting how many times 14 is there in that list", li.count(14))

# To sort the list
li.sort()
print(li)

# We can add a value to the list
li.append("Biswarup")
print(li)

# We can delete the last element using pop function
li.pop()
print(li)

# To add extra element we can do extends method
li.extend([24, 54, 44, 84, 64, 14])
print(li)

'''To empty the list we can use
li.clear()
print(li)'''

# Return the index value :-
print("The index number of 84 is : ", li.index(84))

# Slicing the value of the list
print(li[0:3])

# We can also change the value targeting the index number
li[0] = 444
print(li)
