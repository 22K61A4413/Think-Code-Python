array=list(map(int,input("Enter the list: ").split()))
def bubbleSort(array):
    n=len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print(array)
print("The sorted list is: ")
bubbleSort(array)
                
