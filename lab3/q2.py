#Count occurrences of an element in a list., take user input for element to be counted
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count    
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    element = int(input("Enter the element to count: "))
    occurrences = count_occurrences(num_list, element)
    print(f"The element {element} occurs {occurrences} times in the list.")
    
