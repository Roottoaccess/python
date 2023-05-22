# Here we will know about the concept of while loop
# writing a simple while loop program
i = 0
while i < 5:
    print(i)
    i += 1

print("Program has finished executing .... ")

# Making a fun program !
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    else:
        print("Your entered number is:", number)
print("You have entered 0 that's why the program has been ended....")