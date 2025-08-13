list1=list(map(int,input("Enter elements of list1: ").split()))
list2=list(map(int,input("Enter elements of list1: ").split()))
common_elements=list((set(list1))&(set(list2)))
print("The common elements are: ",common_elements)