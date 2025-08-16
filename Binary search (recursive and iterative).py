def binary_search(arr,key):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1

my_list=list(map(int,input("Enter the elements in the list: ").split()))
my_list.sort() 
key=int(input("Enter the element want to serach in the list: "))
result=binary_search(my_list,key)    

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the list")