#Write a program to check whether a given number is a palindrome., taking input from the user.

def is_palindrome(n):
    num_str = str(n)
    reversed_str = num_str[::-1]
    return num_str == reversed_str

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.") 