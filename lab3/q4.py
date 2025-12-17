#Remove duplicates from a list without using set().
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
# --- IGNORE ---
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    unique_list = remove_duplicates(num_list)
    print(f"List after removing duplicates: {unique_list}")
    
