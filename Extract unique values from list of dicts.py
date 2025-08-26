my_dict = [
    {"id": 1, "value": 100},
    {"id": 2, "value": 200},
    {"id": 3, "value": 100},
    {"id": 4, "value": 300}
]


print("The dictionary elements: ", my_dict)
unique_values = set(val for dic in my_dict for val in dic.values())
print("Unique values:", unique_values)
