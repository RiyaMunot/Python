fibonacii=lambda n:0 if n==0 else 1 if n==1 else (fibonacii(n-1)+fibonacii(n-2))
n=int(input("Enter number"))
for i in range(1,n+1):
    f=fibonacii(i)
    print(f)
