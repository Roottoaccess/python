# From here we will see and learn about the concepts of if else statement
# Making a driving eligiblity program
age = int(input("Enter your current age: "))
print("Thanks for providing your age")
# If , elif, else are known as if else ladder
if age >= 18:
    print("You can drive and have a safe drive")
elif age <=0:
    print("Please enter a valid age !")
elif age <= 15:
    print("You are a kid now !")
else:
    print("You cannot drive now, wait until you get 18")
print("Please visit us again :)")
