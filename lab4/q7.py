#Convert a dictionary to a list of tuples and vice versa.
def dict_to_tuples(input_dict):
    return list(input_dict.items())

def tuples_to_dict(tuple_list):
    return dict(tuple_list)

# Example usage
if __name__ == "__main__":
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original dictionary:", sample_dict)
    
    # Convert dictionary to list of tuples
    tuple_list = dict_to_tuples(sample_dict)
    print("Dictionary as list of tuples:", tuple_list)
    
    # Convert list of tuples back to dictionary
    back_to_dict = tuples_to_dict(tuple_list)
    print("List of tuples as dictionary:", back_to_dict)
    