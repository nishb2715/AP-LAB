#rotate a list left and right by given positions 
def rotate_list(lst, positions, direction='left'):
    n = len(lst)
    positions = positions % n  # Handle positions greater than list length
    if direction == 'left':
        return lst[positions:] + lst[:positions]
    elif direction == 'right':
        return lst[-positions:] + lst[:-positions]
    else:
        raise ValueError("Direction must be 'left' or 'right'") 
# --- IGNORE ---
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    positions = int(input("Enter number of positions to rotate: "))
    direction = input("Enter direction (left/right): ").strip().lower()
    rotated_list = rotate_list(num_list, positions, direction)
    print(f"Rotated List: {rotated_list}")
    