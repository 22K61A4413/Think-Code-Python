list=list(map(int,input("Enter the list of elements: ").split()))
second_largest=sorted(set(list))[-2]
print("The second largest element is: ",second_largest)