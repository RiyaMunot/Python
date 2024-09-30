n=int(input("Enter the range value"))
a=1
b=0
for i in range(0,n+1):
    c=a+b
    print(c)
    a=b
    b=c
