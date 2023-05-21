# This is the program to take random age from users and check whether the person is eligible for vote or not
# Taking the user-name
name = input("Enter your name here : ")
print("Thanks for visiting us ", name)

# Taking the age
age = int(input("Enter your current age : "))

# Checking if the person is eligible to vote or not
if age >= 18:
    print("You are eligible to vote !")
elif age <= 0:
    print("Please enter currect age !")
else:
    print("You are not eligible to vote !")
