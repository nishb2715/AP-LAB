#Validate email format using regex.
import re
email = input("Enter an email address to validate: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
    