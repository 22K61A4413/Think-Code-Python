num=int(input("Enter a number: "))
rev=0
rem=0
while(num>0):
    rem = num % 10         
    rev = rev * 10 + rem   
    num = num // 10         
print("Reverse of number: ",rev)








123
3