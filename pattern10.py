n=int(input("Enter how many lines:"))
for i in range(1,n+1):
    k=1
    for j in range(1,i+1):
        print(k,end=" ")
        if i%2==0:
            k=k+2
        else:
            k=k+1
    print()
