def reverse(str):
    if len(str) == 0:
        return str
    else:
        # recursive case
        return reverse(str[1:]) + str[0]
string=input("Enter the string: ")
print("The original string: ",string)
result=reverse(string)
print("The reverse of given string is: ",result)