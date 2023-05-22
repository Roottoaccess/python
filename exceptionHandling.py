# We will see what is exception handling below
# try and except
# Except as e and then printing e will be show what the error is actually ?
try:
    a = int(input("Enter your number: "))
    print(a + 3)
except Exception as e:
    print("Some error occur during execution of the code please check your input", e)