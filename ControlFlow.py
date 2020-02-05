
# Date: 2.3.20
# Programmer: Landon Baker

# Declare Global Variables here

# name = input("What is your name?: ")
x = 15

# Create Functions Here

# Greeting Function
"""
def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)
"""
# Functions & Local Variable
def printSomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): #Function name = printNumber with a PARAMETER of age.
    print(age)

# Default Parameter Values
def printTwoNumbers(x,y = 71):
    print("First Parameter(Number): " + str(x))
    print("Second Parameter(Number): " + str(y))

# Print Sum
def printSum(x,y):
    print(x + y)

# Print Multiple Times
def printMultipleTimes(string, Times):
    for i in range(Times):
        print(string)

# Call Functions Here
print("\n****Greetings Function****\n")
print("Does not work for me.")
# greeting()

print("\n****Print Something Function****\n")
printSomething()

print("\n****Print Number Function****\n")
printNumber(28)
printNumber(38)

print("\n****Print Two Numbers Function****\n")
printTwoNumbers(23,78)
printTwoNumbers(45)

print("\n****Print Sum Function****\n")
printSum(1,17)

print("\n****Print Multiple Times Function****\n")
printMultipleTimes("I love computer Science", 13)

print("\n****Thank You For Hanging Out With Me Through All Of My Functions Being Called(Except For Greeting, since it does not work.****\n")
