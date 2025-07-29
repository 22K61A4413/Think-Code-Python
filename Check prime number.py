print("Enter a number")
num = int(input())

if num <= 1:
    print("The given number is not a prime number:", num)
else:
    for i in range(2, num+ 1):
        if num % i == 0:
            print("The given number is not a prime number:", num)
            break
    else:
        print("The given number is a prime number:", num)
