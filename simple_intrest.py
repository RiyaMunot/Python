def simple_itr(p,n=1,r=10):
    i=(p*n*r)/100
    return i
p=int(input("Enter principal amount"))
n=int(input("Enter no of years"))
r=int(input("Enter rate"))
SI=simple_itr(p,n,r)
print("SI=",SI)
SI=simple_itr(p,n)
print("SI=",SI)
SI=simple_itr(p)
print("SI=",SI)
