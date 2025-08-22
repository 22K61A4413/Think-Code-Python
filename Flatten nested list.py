import ast

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):  # If element is a list, flatten it
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Dynamic input
user_input = input("Enter a nested list: ")  
nested_list = ast.literal_eval(user_input)   # Convert string -> Python list

# Flatten and print
flat_list = flatten(nested_list)
print("The flattened list is:", flat_list)
