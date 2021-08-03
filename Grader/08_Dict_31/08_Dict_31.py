def total(pocket):
    r=0

    for key in pocket:
        r+=key*pocket[key]
    return r

def take(pocket,money):
    for key in money:
        if key in pocket:
            pocket[key]+=money[key]
        else:
            pocket[key]=money[key]

def pay(pocket,amt):
    r={}

    for key in sorted(pocket,reverse=True):
        if key<=amt:
            if (key*pocket[key]>=amt):
                r[key]=amt//key
                amt%=key
            else:
                r[key]=pocket[key]
                amt-=key*pocket[key]

    if amt==0:
        for key in r:
            pocket[key]-=r[key]
        return r
    else:
        return {}

exec(input().strip())