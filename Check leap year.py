year=int(input("Enter the value of the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The given year is an leap year: ",year)
else:
    print("The given year is not an leap year: ",year)