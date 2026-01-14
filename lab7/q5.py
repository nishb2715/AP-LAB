#Q5.Write a program to create a tuple of even numbers from a given tuple.
given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers_tuple = tuple(num for num in given_tuple if num % 2 == 0)
print("Tuple of even numbers:", even_numbers_tuple)
