import math

n=int(input())

if (n>=1000000000):
    if (n>=10000000000):
        print(str(int(round(n/1000000000,0)))+"B")
    else:
        print(str(round(n/1000000000,1))+"B")
elif (n>=1000000):
    if (n>=10000000):
        print(str(int(round(n/1000000,0)))+"M")
    else:
        print(str(round(n/1000000,1))+"M")
elif (n>=1000):
    if (n>=10000):
        print(str(int(round(n/1000,0)))+"K")
    else:
        print(str(round(n/1000,1))+"K")
else:
    print(str(n))