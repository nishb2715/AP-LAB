#Reverse a list using slicing.
def reverse_list(lst):
    return lst[::-1]      
# --- IGNORE ---
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    reversed_list = reverse_list(num_list)
    print(f"Reversed List: {reversed_list}")
      
