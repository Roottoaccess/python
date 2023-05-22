# Here we will look after the concept of functions
# + new is use to concatenate the string
def greetHello(name, ending):
    print("Hello Master " + name)

    print(ending)
print("Executing function c0de....")
greetHello("Jeet", "Thankyou")
# we can also add another name and reuse this function
greetHello("Hrithik", "Thank !")
print("Done....")

print("Letter Generator........")
# Making a letter generator
# Writing f in front of the string to use the variables inside the string
def letter(name, date):
    st = f"Hello mam, \n I am {name} and I cannot come to school on {date}"
    print(st)

letter("Biswarup", "24th June")

# Making an average calculate program
def average(a,b):
    return (a+b)/2

print("The average value is : ", average(45, 52))