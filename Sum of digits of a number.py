num=int(input("Enter a number: "))
digits=len(str(num))
sum=0
while(num>0):
    rem=num%10
    sum+=rem
    num//=10
print("The sum of digits of a number: ",sum)