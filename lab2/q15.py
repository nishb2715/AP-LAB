#Extract all numbers from a string using regex.
import re
string = input("Enter a string: ")
numbers = re.findall(r'\d+', string)
print(f"Numbers extracted from the string: {numbers}")
