# Date: 1.20.20
# Program: Double For Loop

for i in range(3):
    print("Outer For Loop " + str(i))
    for k in range(4):
        print("\tInner For Loop " + str(k))

# Programmer: Landon Baker
# Date: 12.16.19
# Program: Guess My Number


MyNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess.
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to MyNumber.
while guess != MyNumber:
    print("\nNo, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongratulations on guessing my number\n")


"""
Programmer: Landon Baker
Date: 1.23.20
Program: While Loop Nested Inside Of A For Loop
"""

for i in range(4):
    print("For Loop: " + str(i))
    print("")
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
        x = x - 1

# Programmer: Landon Baker
# Date: 12.16.19
# Program: 1 Through 10


x = 1

# While loop will see if a condition has been met
# If not, it will run again until the condition has been met.

while x <= 10:
    print(x)
    x += 1

print("\n ********************\n")

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