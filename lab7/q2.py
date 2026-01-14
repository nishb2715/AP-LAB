#Write a program to search for a specific word in a file and display the line numbers.
def search_word_in_file(filename, target_word):
    line_numbers = []
    with open(filename, "r") as file:
        for line_num, line in enumerate(file, 1):
            if target_word in line:
                line_numbers.append(line_num)
    return line_numbers

filename = "student_details.txt"
target_word = "Alice"
line_numbers = search_word_in_file(filename, target_word)
if line_numbers:
    print(f"The word '{target_word}' was found on lines: {line_numbers}")
else:
    print(f"The word '{target_word}' was not found in the file.")