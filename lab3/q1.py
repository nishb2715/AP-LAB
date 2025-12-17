#Find the maximum and minimum in a list, take user input of the lists
def find_max_min(lst):
    if not lst:
        return None, None
    maximum = lst[0]
    minimum = lst[0]
    for item in lst:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum = item
    return maximum, minimum

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    maximum, minimum = find_max_min(num_list)
    print(f"Maximum: {maximum}, Minimum: {minimum}")






