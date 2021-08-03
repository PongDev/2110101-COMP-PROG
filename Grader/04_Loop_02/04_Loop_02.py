n=float(input())

L=0
U=n
mid=(L+U)/2
while abs(n-(10**mid))>(10**-10)*max(n,10**mid):
    if (10**mid<n):
        L=mid
    else:
        U=mid
    mid=(L+U)/2
print(round(mid,6))