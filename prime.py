no=int(input("Enter a no:"))
flag=True
for n in range(2,no):
    if no%n==0:
        flag=False
        break
if flag:  #flag==True
    print("No is prime")
else:
    print("No is not prime")
