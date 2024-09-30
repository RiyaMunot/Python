for i in range(1,100+1):
    flag=True
    for j in range(2,i-1):
        if i%j==0:
            flag=False
            break
    if(flag):
        print(i)
