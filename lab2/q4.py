#Compute square, cube, and √n using the math library.
import math
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
square_root = math.sqrt(num)
print(f"Square of {num} is {square}")
print(f"Cube of {num} is {cube}")
print(f"Square root of {num} is {square_root}")
