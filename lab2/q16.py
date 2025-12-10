#Print a diamond pattern using loops.
n = int(input("Enter the number of rows for the diamond pattern: "))
# Upper part of diamond
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
# Lower part of diamond
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
        