# # From here we will learn about dictionary
# This is an empty dictionary
# dict1 = {}
# # How to make a empty set then
# a = set()
# print(dict1, type(dict1))
# print(a, type(a))

# Dictionary are consider of key value pair
dict1 = {"good": "something pleasent", "fetch": "to bring", "1": "the number 1"}
# Printing the full dictionary
print(dict1)
# Calling the key and printing the value of the key value pair
print(dict1["good"])
print(dict1["1"])
# storing the marks of student in dictionary
student = {
    "Jeet": 98,
    "Harry": 88,
    "Bob": 78,
    "John": 54,
    "Hrithik": 94
}
print("The marks obtained by jeet is :", student["Jeet"])
print("The marks obtained by hrithik is :", student["Hrithik"])

# Dictionary method
# Is dictionary mutable or non-mutable ? it is mutable we can change
# To add one more member in student dictionary we will do
student["Duggu"] = 88
print(student)

# get method in dictionary
# The advantage of the get method is if no key present then it will not show an error rather it will show 'None'
print(student.get("Priyanka"))
print(student.get("Hrithik"))
# To see every key in the dictionary we will use:-
print(student.keys())
# To pop the last element we will use
print("After deleting the last element:", student.popitem())
# To display the marks or the values of the keys
print(student.values())
# To display the tupples in the dictionary
print(student.items())





