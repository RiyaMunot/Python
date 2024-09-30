n=int(input("Enter a number:"))
ct=0
sum=0
temp=n
while n!=0:
    digit=n%10
    n=n//10
    ct=ct+1
n=temp
print("Count=",ct)
while n!=0:
    digit=n%10
    n=n//10
    sum=sum+digit**ct
if sum==temp:
    print("Your no. is armstrong no.",sum)
else:
    print("Your number is not armstrong number")
