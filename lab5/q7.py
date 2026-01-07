#Use reduce() to compute the product of list items.
from functools import reduce
def product_of_list(lst):
    return reduce(lambda x, y: x * y, lst)
#usage
numbers = [1, 2, 3, 4]
result = product_of_list(numbers)
print("The product of the list items is:", result)
