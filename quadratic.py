#quadratic equation
import math
a=int(input("Enter first no."))
b=int(input("Enter second no."))
c=int(input("Enter third no."))
d=(b**2)-(4*a*c)
if d>0:
    r1=(-b+(math.sqrt(d)))/2*a
    r2=(-b+(math.sqrt(d)))/2*a
    print("Roots are:",r1,"\t",r2)
else:
    print("roots are imaginary")

