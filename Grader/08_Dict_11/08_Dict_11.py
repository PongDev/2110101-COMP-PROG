def reverse(d):
    r={}

    for key in d:
        r[d[key]]=key
    return r

def keys(d,v):
    r=[]

    for key in d:
        if d[key]==v:
            r.append(key)
    return r

exec(input().strip())