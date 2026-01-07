#Count occurrence of each word and store the output in a new file.
from collections import Counter
def count_word_occurrences(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    
    words = text.split()
    word_count = Counter(words)
    
    with open(output_file, 'w') as f:
        for word, count in word_count.items():
            f.write(f"{word}: {count}\n")
#usage
count_word_occurrences('input.txt', 'output.txt')