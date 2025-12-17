#Check if a string is palindrome.
string = input("Enter a string: ")
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
if string == reversed_string:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")

    