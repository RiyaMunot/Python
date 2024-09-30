a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
temp1=a
temp2=b
while a!=b:
    if(a<b):
        a=a+temp1
    else:
        b=b+temp2
print("LCM=",a)
