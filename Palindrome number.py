number=int(input("Enter  a number "))
rev=0
rem=0
temp=number
while(number>0):
    rem=number%10
    rev=rev*10+rem
    number//=10
if (temp==rev):
    print("The given number is a palindrome: ",temp)
else:
    print("The given number is not a palindrome: ",temp)