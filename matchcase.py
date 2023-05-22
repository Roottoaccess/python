# From here we will look after the match case topic in python
# Match case are newly introduce in python
# Match case is similar to switch statement
print("Match case in Python Programming")
number = 2
match( number ):
    case 1:
        print("Number is 1")
    case 2:
        print("number is 2")
    case _:
        print("Default")
# Making a program to make a calculator
# print("Basic calculator !")
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# operation = input("Input the operation to compute only from(+,-,*,/): ")
#
# match operation:
#     case '+':
#         print("Result: ", number1 + number2)
#     case '-':
#         print("Result: ", number1 - number2)
#     case '*':
#         print("Result: ", number1 * number2)
#     case '/':
#         print("Result: ", number1 / number2)
# # we can use case_: for handling the default conditions
#     case _:
#         print("Please enter a valid operation !")


# Write a python program to print table of a number which lies between 1 - 10
print("Table generator from 1 to 10")
user = int(input("Enter any number between 1 to 10 to print the table of it: "))

match user:
    case 1:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 2:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 3:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 4:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 5:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 6:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 7:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 8:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 9:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case 10:
        for i in range(1, 11):
            result = user * i
            print(user, "X", i, "=", result)
    case _:
        print("Enter valid number !")
