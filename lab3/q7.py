#find common elements between 2 lists
def common_elements(lst1, lst2):
    common_list = []
    for item in lst1:
        if item in lst2:
            common_list.append(item)
    return common_list  
# --- IGNORE ---
if __name__ == "__main__":
    user_input1 = input("Enter numbers for the first list separated by spaces: ")
    user_input2 = input("Enter numbers for the second list separated by spaces: ")
    list1 = list(map(int, user_input1.split()))
    list2 = list(map(int, user_input2.split()))
    common_list = common_elements(list1, list2)
    print(f"Common Elements: {common_list}")