#Reverse a string without using slicing.
string = input("Enter a string to reverse: ")
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(f"The reversed string is: {reversed_string}")
