print("Pattern 1")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

print()

print("Pattern 2")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

print()

print("Pattern 3")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print()

print("Pattern 4")
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()
