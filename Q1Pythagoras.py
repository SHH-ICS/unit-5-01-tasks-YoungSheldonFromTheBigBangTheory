# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

while True:
    a = input("Input side A: ")
    try:
        a = float(a)
    except ValueError:
        print("\nInvalid input. Enter side length.\n")
        continue

    b = input("Input side B: ")

    try:
        b = float(b)
    except ValueError:
        print("\nInvalid input. Enter side length.\n")
        continue

    x = math.sqrt((a**2) + (b**2))

    print(str(x))

    break