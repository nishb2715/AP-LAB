#Read a text file and count characters.
file_path = 'C:\\Users\\NISHTHA\\Desktop\\sample.txt'  
try:
    with open(file_path, 'r') as file:
        content = file.read()
        char_count = len(content)
        print(f'The file contains {char_count} characters.')
except FileNotFoundError:
    print(f'The file at {file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')
