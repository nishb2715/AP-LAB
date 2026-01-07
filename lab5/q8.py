#Write a function using default and keyword arguments.
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

#usage
print(greet("Alice")) 
print(greet("Bob", "Hi"))  
print(greet("Charlie", "Good morning", "?"))  
