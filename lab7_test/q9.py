#Q9.Write a program to count the number of lines, words, and characters in a file.
def count_file_stats(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count

filename = input("Enter the filename: ")
lines, words, chars = count_file_stats(filename)
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")