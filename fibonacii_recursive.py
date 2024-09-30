def fibonacii(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fibonacii(n-1)+fibonacii(n-2))
        
n=int(input("Enter number"))
for i in range(1,n+1):
    f=fibonacii(i)
    print(f)
from functools import reduce
fact=lambda n:reduce(lambda f,i:f*i,range(1,n+1))
n=int(input("Enter value"))
f=fact(n)
print("fact=",f)
