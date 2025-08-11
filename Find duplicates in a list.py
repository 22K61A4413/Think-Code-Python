nums=list(map(int,input("Enter the list: ").split()))
duplicates=list(set([x for x in nums if nums.count(x)>1]))
print("Duplicate elements: ",duplicates)