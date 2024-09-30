n=int(input("How many lines?"))
sp=n
for i in range(1,n+1):
    for j in range(1,sp):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
    sp=sp-1
