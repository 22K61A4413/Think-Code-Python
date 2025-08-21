def pow_of_number(num,pow):
    if pow==0:
        return 1
    return num*pow_of_number(num,pow-1)

number,power=map(int,input("Enter the number,power: ").split())
result=pow_of_number(number,power)
print(f"The Power of number using recursion is: ",result)