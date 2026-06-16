#Print all Armstrong numbers in a given range.
lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))
print(f"Armstrong numbers between {lower} and {upper} are:")
for num in range(lower, upper + 1):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    if sum_of_powers == num:
        print(num)
        