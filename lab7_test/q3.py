#Q3.Write a program to count vowels, consonants, digits, and special characters in a string, taking input from the user.

def count_characters(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return vowel_count, consonant_count, digit_count, special_count

string = input("Enter a string: ")
vowels, consonants, digits, specials = count_characters(string)
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Special Characters: {specials}")