import math
no=int(input("Enter no to check:"))
sq=int(math.sqrt(no))
print(sq)
if sq*sq==no:
    print("No. is perect square")
else:
    print("no is not perfect square")
    sq=sq+1
    least=sq*sq-no
    print("The least value to be added to make no perfect square=",least
          )
