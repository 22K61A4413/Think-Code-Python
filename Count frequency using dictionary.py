input=list(map(int,input("Enter the list elements: ").split()))
frequency={}
for i in input:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print("the frequency of eacjh element is: ",frequency)
