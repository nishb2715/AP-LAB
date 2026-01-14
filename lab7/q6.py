#Q6.Write a program to sort a dictionary by its values in ascending order.
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5, 'elderberry': 4}
sorted_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values in ascending order:", sorted_dict)
    