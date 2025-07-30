def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example: Generate first 10 Fibonacci numbers
num = int(input("Enter how many terms: "))
fibonacci(num)
