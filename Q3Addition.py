# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import math
import random

while True:

    a = random.randint(1, 100)
    b = random.randint(1, 100)

    y = input(str(a) + "+" + str(b) + "= ")

    if int(y) == int(a+b):
        print("Correct")
    else:
        print("Incorrect")

    p = input("Play again. y/n: ")
    if p == "n":
        break
    
