#progra to find the factorrial of a given number
num = int(input("Enter a number to find its factorial: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1.")
else:
    for i in range(2, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")

    