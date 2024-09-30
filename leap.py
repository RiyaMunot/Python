year=int(input("Enter year to check:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("Year:",year,"is a leap year")
else:
    print("Year:",year,"is a not leap year")

