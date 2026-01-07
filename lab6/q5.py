#Read a file and remove punctuation.
import string
def remove_punctuation(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            translator = str.maketrans('', '', string.punctuation)
            cleaned_content = content.translate(translator)
            return cleaned_content
    except FileNotFoundError:
        return "File not found."
#usage:
file_path = "C:\\Users\\NISHTHA\\Desktop\\sample.txt"  # Replace with your file path
cleaned_text = remove_punctuation(file_path)
print(cleaned_text)
