n=float(input())

tmp=n
L=0
U=0
while tmp>0:
    tmp//=10
    U+=1
mid=(L+U)/2
while abs(n-(10**mid))>(10**-10)*max(n,10**mid):
    if (10**mid<n):
        L=mid
    else:
        U=mid
    mid=(L+U)/2
print(round(mid,6))