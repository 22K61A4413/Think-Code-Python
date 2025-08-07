def triangle(n):
    for i in range(1,n+1):
        print("* "*i)

def pyramid(n):
    for i in range(n+1):
        print(" " * (rows-i)+"* "*i)

rows=int(input("Enter number of rows: "))
triangle(rows)
pyramid(rows)