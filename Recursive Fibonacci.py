def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

number=int(input("Enter the number: "))

print(f"The fibonacci series of given number {number}")
for i in range(number):
    print(fibonacci(i), end=" ")