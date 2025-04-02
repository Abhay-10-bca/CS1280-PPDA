
def get_dictionary(num):
    n = int(input(f"Enter the number of key-value pairs for Dictionary {num}: "))
    dictionary = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        
        # Try converting values to numbers if possible
        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():
            value = float(value)
        
        dictionary[key] = value
    return dictionary


def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    
    for key, value in dict2.items():
        if key in merged_dict:
            # If both values are numbers, add them
            if isinstance(merged_dict[key], (int, float)) and isinstance(value, (int, float)):
                merged_dict[key] += value
            # If both values are strings, concatenate them
            elif isinstance(merged_dict[key], str) and isinstance(value, str):
                merged_dict[key] += " " + value
            else:
                # If different data types, store them as a list
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value  # If key is unique, just add it
            
    return merged_dict


print("Enter values for the first dictionary:")
dict1 = get_dictionary(1)

print("\nEnter values for the second dictionary:")
dict2 = get_dictionary(2)


merged_dict = merge_dictionaries(dict1, dict2)


print("\nMerged Dictionary:", merged_dict)
