#Copy content from one file to another.
source_file_path = "C:\\Users\\NISHTHA\\Desktop\\sample.txt"
destination_file_path = "C:\\Users\\NISHTHA\\Desktop\\destination.txt"
try:
    with open(source_file_path, 'r') as source_file:
        content = source_file.read()
    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(content)
    print('Content copied successfully.')
except FileNotFoundError:
    print(f'The file at {source_file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')