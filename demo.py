sprice=int(input("Enter Shopping price"))
if sprice>=1000 and sprice<2000:
    disc=sprice*10/100
elif sprice>=2000 and sprice<3000:
    disc=sprice*20/100
elif sprice>=3000:
    disc=sprice*30/100
else:
    disc=0
totalsp=sprice-disc
print("Discounted Shopping price=",totalsp)
