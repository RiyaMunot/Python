for i in range(1,100+1):
    temp=i
    sum=0
    while i>0:
        digit=i%10
        i=i//10
        sum=sum*10+digit
    if(sum==temp):
        print(sum)
