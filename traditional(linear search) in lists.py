my_list=list(map(int,input("Enter the elements for the list: ").split()))
n=len(my_list)
key=int(input("Enter the element to search: "))
found=False
for i in range(n):
    if my_list[i]==key:
        print(f"The element:{key} is found in list:{my_list} the position is:{i}")
        found=True
        break
if not found:
    print("The element is not found in the list")