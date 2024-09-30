n= int(input("Enter how many lines"))
for i in range(1,n+1):
    if i%2==0:
        temp=97
    else:
        temp=65
    for j in range(temp,temp+i):
        print(chr(j),end=" ")
        if i%2==0:
            j=j+2
        else: j=j+1
    print()
    
    
