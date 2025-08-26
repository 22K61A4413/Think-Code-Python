from itertools import zip_longest
list1 = input("Enter the key list: ").split()
list2 = list(map(int, input("Enter the values: ").split()))
new_dict = dict(zip_longest(list1, list2, fillvalue=None))
print("New Dictionary: ", new_dict)
