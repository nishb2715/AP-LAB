#Sort a dictionary by keys and values.
def sort_dict(input_dict):
    # Sorting by keys
    sorted_by_keys = dict(sorted(input_dict.items()))
    
    # Sorting by values
    sorted_by_values = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    
    return sorted_by_keys, sorted_by_values
#usage
if __name__ == "__main__":
    sample_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    sorted_keys, sorted_values = sort_dict(sample_dict)
    print("Sorted by keys:", sorted_keys)
    print("Sorted by values:", sorted_values)
