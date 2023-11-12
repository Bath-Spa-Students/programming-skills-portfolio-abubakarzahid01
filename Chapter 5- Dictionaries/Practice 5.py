#Write a Python program to merge two dictionaries into one.
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}
dict1 = {'a': 11, 'b': 12}
dict2 = {'c': 13, 'd': 14}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)