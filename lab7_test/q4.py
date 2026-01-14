#Q4.Write a program to remove duplicate elements from a list while preserving order, taking input from the user.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

user_input = input("Enter a list of elements separated by spaces: ")
elements = user_input.split()
unique_elements = remove_duplicates(elements)
print("List with duplicates removed:", unique_elements)