
def get_dictionary(num):
    n = int(input(f"Enter the number of key-value pairs for Dictionary {num}: "))
    dictionary = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value
    return dictionary


print("Enter values for the first dictionary:")
dict1 = get_dictionary(1)

print("\nEnter values for the second dictionary:")
dict2 = get_dictionary(2)


merged_dict = {**dict1, **dict2}  # Using dictionary unpacking


print("\nMerged Dictionary:", merged_dict)
