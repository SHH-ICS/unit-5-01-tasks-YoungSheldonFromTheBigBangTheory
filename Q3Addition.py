# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import math
import random

while True:

    a = random.randint(1, 100)
    b = random.randint(1, 100)

    while True:
        y = input(str(a) + "+" + str(b) + "= ")
        try:
            y = int(y)
        except ValueError:
            print("Invalid. Not a number.")
            continue
        break

    if int(y) == int(a+b):
        print("Correct")
    else:
        print("Incorrect")

    p = input("Play again. y/n: ")
    while p != "y" and p != "n":
        print("\nInvalid. Play again. y/n: \n")
        p = input("Play again. y/n: ")

    if p == "n":
        print("\nThanks for playing!\n")
        break