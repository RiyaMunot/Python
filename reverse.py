n=int(input("Enter a number"))
sum=0
while n!=0:
    digit=n%10
    sum=sum*10+digit
    n=n//10
print("Reverse digit=",sum)
