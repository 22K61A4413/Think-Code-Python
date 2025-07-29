def solve(num):
    fact = 1
    if num <= 1:
        print("The factorial of number is: 1")
    else:
        for i in range(2, num + 1):
            fact *= i
        print("The factorial of number is:", fact)

num = int(input("Enter a Number: "))
solve(num)
