#Accept a number and check if it is prime or composite.
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is neither prime nor composite.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is a composite number.")
            break
    else:
        print(f"{num} is a prime number.")
        