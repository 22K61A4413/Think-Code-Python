from collections import Counter
my_list=list(map(int,input("Enter the elements: ").split()))
freq=Counter(my_list)
print("The frequency of elements in list is: ",freq)