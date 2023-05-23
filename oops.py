# Learning about the oops concept
class Employee:
    # salary = 88
    # name = "Rohan"

    # This is a constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        # return self.salary
        print(self.salary)
    def getName(self):
        print(self.name)
# Calling the following classes and object
jeet = Employee("Jeet", "78,994")
# print("The salary of Jeet is:", jeet.salary)
# print("The name of the user is:", jeet.name)
jeet.getSalary();
jeet.getName();

harry = Employee("Harry", "58,000")
print("The salary of Harry is:", harry.salary)
print("The name of the user is:", harry.name)
tom = Employee("Tom", "70,000")
print("The salary of tom is:", tom.salary)
print("The name of the user is:", tom.name)