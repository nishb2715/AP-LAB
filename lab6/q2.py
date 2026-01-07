#Append data to a file.
file_path = 'C:\\Users\\NISHTHA\\Desktop\\sample.txt'  
data_to_append = '\nThis is the new line to be appended.'   
try:
    with open(file_path, 'a') as file:
        file.write(data_to_append)
        print('Data appended successfully.')
except FileNotFoundError:
    print(f'The file at {file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')
    