#Print star patterns (triangle, inverted triangle).
n = int(input("Enter the number of rows for the star patterns: "))
print("Triangle Pattern:")
for i in range(1, n + 1):
    print('* ' * i)
print("Inverted Triangle Pattern:")
for i in range(n, 0, -1):
    print('* ' * i)
    