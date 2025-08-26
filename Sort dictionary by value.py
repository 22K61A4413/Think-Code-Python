my_dict={}
n=int(input("Enter number of elements: "))
for i in range(n):
    key=int(input("Enter key value: "))
    value=int(input("Enter value: "))
    my_dict[key]=value
print("The dictinar elements: ",my_dict)
sorted_order=dict(sorted(my_dict.items(),key=lambda item: item[1]))
print("Sorted dictionary: ",sorted_order)