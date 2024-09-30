
no=int(input("Enter the number:"))
fact=1
while(no>0):
    fact=fact*no
    no=no-1
print("Factorial of number=",fact)








no=int(input("Enter the number:"))
fact=1
for i in range(1,no+1):
    fact=fact*i
print("Factorial of number=",fact)
