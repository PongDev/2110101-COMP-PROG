def first_fit(L,e):
    for lst in L:
        if (sum(lst)+e<=100):
            lst.append(e)
            break
    else:
        L.append([e])

def best_fit(L,e):
    mnleft=100
    mnidx=-1
    for idx,lst in enumerate(L):
        left=100-sum(lst)-e
        if (left>=0 and left<mnleft):
            mnleft=left
            mnidx=idx
    if mnidx==-1:
        L.append([e])
    else:
        L[mnidx].append(e)

def partition_FF(D):
    L=[]

    for e in D:
        first_fit(L,e)
    return L

def partition_BF(D):
    L=[]

    for e in D:
        best_fit(L,e)
    return L

exec(input().strip())