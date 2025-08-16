my_list=list(map(int,input("Enter the elements: ").split()))
odd_count=0
even_count=0
for i in range(len(my_list)):
    if my_list[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"The even numbers count in list: {even_count}\nThe odd numbers count in list: {odd_count}")
