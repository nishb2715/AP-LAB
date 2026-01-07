#Count lines, words, and characters in a file.
file_path = 'C:\\Users\\NISHTHA\\Desktop\\sample.txt'
try:
    with open(file_path, 'r') as file:
        content = file.readlines()
        line_count = len(content)
        word_count = sum(len(line.split()) for line in content)
        char_count = sum(len(line) for line in content)
        print(f'The file contains {line_count} lines, {word_count} words, and {char_count} characters.')
except FileNotFoundError:
    print(f'The file at {file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')

    