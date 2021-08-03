def convex_polygon_area(p):
    r=0

    for i in range(len(p)):
        r+=p[i][0]*p[(i+1)%len(p)][1]
        r-=p[i][0]*p[i-1][1]
    return abs(0.5*r)

def is_heterogram(s):
    hsh={}

    for i in s.lower():
        if "a"<=i<="z":
            if i in hsh:
                return False
            else:
                hsh[i]=True
    return True

def replace_ignorecase(s,a,b):
    r=s
    tmpFind=a.lower()
    pos=0
    while True:
        pos=r.lower().find(tmpFind,pos)
        if (pos==-1):
            return r
        else:
            r=r[:pos]+b+r[pos+len(a):]
            pos+=len(b)

def top3(votes):
    return [key for value,key in (sorted([[-votes[key],key] for key in votes])[:3])]

for k in range(2):
    exec(input().strip())