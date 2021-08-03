n=int(input())
unionSet=None
intersectSet=None
for i in range(n):
    data=[int(e) for e in input().split()]
    if unionSet==None:
        unionSet=set(data)
    else:
        unionSet=unionSet.union(data)
    if intersectSet==None:
        intersectSet=set(data)
    else:
        intersectSet=intersectSet.intersection(data)
if n==0:
    print(0)
    print(0)
else:
    print(len(unionSet))
    print(len(intersectSet))