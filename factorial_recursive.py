def factorial(n):
    if n==0:
        return 1
    else:
        f=n*factorial(n-1)
        return f
n=int(input("Enter number"))
f=factorial(n)
print("Factorial of",n,"is=",f)
