#Write a recursive function to compute Fibonacci numbers.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#usage:
n = 10
print(f"Fibonacci number at position {n} is {fibonacci(n)}")

