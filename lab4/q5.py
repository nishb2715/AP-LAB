#Remove duplicates from a list using a set.
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    # Convert the set back to a list
    unique_list = list(unique_set)
    return unique_list
# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print("Original list:", sample_list)
    print("List after removing duplicates:", remove_duplicates(sample_list))
    
