#Q5.Write a program to create a tuple of even numbers from a given tuple.
def even_numbers_tuple(numbers):
    even_nums = tuple(num for num in numbers if num % 2 == 0)
    return even_nums

user_input = input("Enter a tuple of numbers separated by spaces: ")
numbers = tuple(map(int, user_input.split()))
even_tuple = even_numbers_tuple(numbers)
print("Tuple of even numbers:", even_tuple)