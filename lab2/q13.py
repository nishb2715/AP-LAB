#Remove duplicates from a string.
string = input("Enter a string: ")
unique_chars = ''
for char in string:
    if char not in unique_chars:
        unique_chars += char
print(f"String after removing duplicates: {unique_chars}")


