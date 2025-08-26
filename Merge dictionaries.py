dict1={}
n=int(input("Enter number of elements: "))
for i in range(n):
    key=int(input("Enter key value: "))
    value=int(input("Enter value: "))
    dict1[key]=value
print("The dictinar elements: ",dict1)

dict2={}
m=int(input("Enter number of elements: "))
for i in range(m):
    key=int(input("Enter key value: "))
    value=int(input("Enter value: "))
    dict2[key]=value
print("The dictinar elements: ",dict1)

dict1.update(dict2)
merged_dict=dict1
print(f"The dictionaries are: \n {dict1}\n{dict2}")
print("The updated dict is: ",merged_dict)