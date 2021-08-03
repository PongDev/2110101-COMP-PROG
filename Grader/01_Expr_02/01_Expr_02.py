import math

a=float(input())
b=float(input())
c=float(input())

x1=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
x2=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
x1=round(x1,3)
x2=round(x2,3)
print(x1,x2)