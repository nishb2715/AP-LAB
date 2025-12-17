#1. Reverse a string without using slicing.
string = input("Enter a string: ")
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")
