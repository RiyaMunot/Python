n=int(input("Enter how many lines:"))
sp=n
for i in range(1,n+1):
    for j in range(1,sp+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    sp=sp-1
