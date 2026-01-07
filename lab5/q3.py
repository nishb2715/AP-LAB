#Use lambda to filter even numbers from a list.take a list of numbers as input and return a list of even numbers.
def filter_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers
#usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)


