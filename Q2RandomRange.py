# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import math
import random
while True:
    a = input("Input 1st number: ")
    try:
        a = int(a)
    except ValueError:
        print("\nInvalid input.\n")
        continue

    b = input("Input 2nd number: ")
    try:
        b = int(b)
    except ValueError:
        print("\nInvalid input.\n")
        continue

    a2 = min(a, b)
    b2 = max(a, b)

    x = random.randrange(a2, b2)

    print("\n" + str(x))

    break