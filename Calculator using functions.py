def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Divisible by zero"
    return x / y

def mod(x, y):
    return x % y

def calculator():
    print("Select operation:-")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")

    operation = input("Enter a number [1,2,3,4,5]: ")

    if operation in ['1', '2', '3', '4', '5']:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))

        if operation == '1':
            print("Result:", add(first_num, second_num))
        elif operation == '2':
            print("Result:", sub(first_num, second_num))
        elif operation == '3':
            print("Result:", mul(first_num, second_num))
        elif operation == '4':
            print("Result:", div(first_num, second_num))
        elif operation == '5':
            print("Result:", mod(first_num, second_num))
    else:
        print("Invalid input")
calculator()

