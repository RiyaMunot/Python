'''for i in range(100,400+1):
    flag=True
    n=i
    while n>0:
        digit=n%10
        n=n//10
        if digit%2==0:
            flag=False
            break
    if flag:
        print(i)'''
for i in range(100,400+1):
    n=str(i)
    if int(n[0])%2==0 and int(n[1])%2==0 and int(n[2])%2==0:
        print(n)
