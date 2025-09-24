number=int(input("Enter a number: "))
n=len(str(number))
temp=number
sum=0
while(temp>0):
    digit=temp%10
    sum+=digit**n
    temp//=10
if sum==number:
    print(f"The given number is an armstrong number: {number}")
else:

    print(f"The given number is not an armstrong number: {number}")
