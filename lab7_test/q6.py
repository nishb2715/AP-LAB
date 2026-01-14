#Q6.Write a program to find the key with the maximum value in a dictionary.
def max_key_in_dict(d):
    if not d:
        return None
    return max(d, key=d.get)

user_input = input("Enter a dictionary in the format 'key1:value1 key2:value2 ...': ")
dict_items = user_input.split()
d = {}
for item in dict_items:
    key, value = item.split(':')
    d[key] = int(value)

max_key = max_key_in_dict(d)
print(f"The key with the maximum value is: {max_key}")                                                                                                                                                                                                                                                                                                            