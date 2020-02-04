
# Programmer: Landon Baker
# Date: 1.20.20
# Program: Double For Loop

for i in range(3):
    print("Outer For Loop " + str(i))
    for k in range(4):
        print("\tInner For Loop " + str(k))



print("\n ********************\n")

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
