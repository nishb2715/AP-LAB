#Q8.Write a program to read a file and remove blank lines.
def remove_blank_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    non_blank_lines = [line for line in lines if line.strip()]
    return non_blank_lines

filename = input("Enter the filename: ")
lines = remove_blank_lines(filename)
print("Lines without blank lines:")
for line in lines:
    print(line, end='')