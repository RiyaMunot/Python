no=int(input("Enter the value to check:"))
sum=0
temp=no
for i in range(1,no):
    if no%i==0:
        sum=sum+i
if temp==sum:
    print("No. is perfect")
else:
    print("No. is not perfect")
