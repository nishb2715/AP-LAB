#Count the frequency of words in a sentence.
sentence = "This is a test. This test is only a test."
words = sentence.lower().replace('.', '').split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)
