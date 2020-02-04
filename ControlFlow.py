
# Date: 2.3.20
# Programmer: Landon Baker

# Declare Global Variables here

# name = input("\nWhat is your name?: ")
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

# greeting()
# printSomething()
# print(x)
# printNumber(28)
# printNumber(38)
# printTwoNumbers(23,78)
# printTwoNumbers(45)
# printSum(1,17)
printMultipleTimes("I love computer Science", 13)