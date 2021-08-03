def to_Thai(n):
    translator=[
        "soon",
        "neung",
        "song",
        "sam",
        "si",
        "ha",
        "hok",
        "chet",
        "paet",
        "kao"
    ]
    r=[]

    if (n<=1):
        return translator[n]
    if (n>=1000):
        r.append(translator[n//1000])
        r.append("pun")
        n%=1000
    if (n>=100):
        r.append(translator[n//100])
        r.append("roi")
        n%=100
    if (n>=10):
        if (n//10==2):
            r.append("yi")
        elif (n//10>2):
            r.append(translator[n//10])
        r.append("sip")
        n%=10
    if (n>0):
        if (n==1):
            r.append("et")
        else:
            r.append(translator[n])
    return " ".join(r)

exec(input().strip())