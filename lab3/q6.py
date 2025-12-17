#merge two lists without using the + operator 
def merge_lists(lst1, lst2):
    merged_list = []
    for item in lst1:
        merged_list.append(item)
    for item in lst2:
        merged_list.append(item)
    return merged_list
# --- IGNORE ---
if __name__ == "__main__":
    user_input1 = input("Enter numbers for the first list separated by spaces: ")
    user_input2 = input("Enter numbers for the second list separated by spaces: ")
    list1 = list(map(int, user_input1.split()))
    list2 = list(map(int, user_input2.split()))
    merged_list = merge_lists(list1, list2)
    print(f"Merged List: {merged_list}")
