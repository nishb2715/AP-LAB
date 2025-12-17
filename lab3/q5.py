#sort a list in ascending and descending order 
def sort_list(lst):
    ascending = sorted(lst)
    descending = sorted(lst, reverse=True)
    return ascending, descending
# --- IGNORE ---
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    ascending, descending = sort_list(num_list)
    print(f"Ascending order: {ascending}")
    print(f"Descending order: {descending}")
    
