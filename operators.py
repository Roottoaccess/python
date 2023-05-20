# Here we are going to see the different operators in python
number = 15.8
number1 = 18.8
x = 2
y = 5
print("The number = 15.8")
print("The number1 = 18.8")
# Performing arithmetic operations
print("Performing addition = ", number + number1)
print("Performing subtraction = ", number - number1)
print("Performing multiply = ", number * number1)
print("Performing divide = ", number / number1)
print("Performing modules = ", number % number1)
print("Performing x to the power y = ", y ** x)
print("Performing // means that number // number1 = ", number // number1)

# Assignment operator
a = 5
a *= 5
print("Here a is the assignment operator ", a)

# Comparison Operator
com = 45
bom = 55
print("Is 45 is greater than 55 ? ", com > bom)
print("Is 45 is less than 55 ? ", com < bom)
print("Is 45 is not equals to 55 ? ", com != bom)
print("Is 45 is equals to 55 ? ", com == bom)

# Logical Operators
print("45 is greater than 55 and 45 not equals to 55 ? ", com > bom and com != bom)
print("45 is greater than 55 or 45 not equals to 55 ? ", com > bom or com != bom)
print(not(False))
print(not(True))


