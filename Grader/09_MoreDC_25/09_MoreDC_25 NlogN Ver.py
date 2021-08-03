def row_number(t,e):
    for idx,row in enumerate(t):
        if e in row:
            return idx

def flatten(t):
    r=[]

    for row in t:
        for data in row:
            if (data!=0):
                r.append(data)
    return r

def inversions(x):
    # r=0
    # for i in range(len(x)):
    #     for j in range(i+1,len(x)):
    #         if x[i]>x[j]:
    #             r+=1
    # return r
    fenwickTree=[0]*(max(x)+1)

    def add(idx,v):
        while idx<len(fenwickTree):
            fenwickTree[idx]+=v
            idx+=(idx&-idx)
    
    def query(idx):
        r=0

        while idx>0:
            r+=fenwickTree[idx]
            idx-=(idx&-idx)
        return r
    
    countInversion=0

    for e in x[::-1]:
        countInversion+=query(e-1)
        add(e,1)
    return countInversion

def solvable(t):
    inversionMod=inversions(flatten(t))%2
    zeroPosRowMod=row_number(t,0)%2
    return (len(t)%2==1 and inversionMod==0) or\
        (len(t)%2==0 and ((inversionMod==1 and zeroPosRowMod==0) or (inversionMod==0 and zeroPosRowMod==1)))

exec(input().strip())