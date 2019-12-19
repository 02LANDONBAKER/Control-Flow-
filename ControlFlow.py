"""
Programmer: Landon Baker
Date: 12.16.19
Program: Guess My Number
"""

MyNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess.

guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to MyNumber.

while guess != MyNumber:
    print("\nNo, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongratulations on guessing my number")
