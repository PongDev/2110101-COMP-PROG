def make_int_list(x):
    r=[]

    for i in x.split():
        r.append(int(i))
    return r

def is_odd(e):
    return e%2==1

def odd_list(alist):
    r=[]

    for i in alist:
        if (i%2==1):
            r.append(i)
    return r

def sum_square(alist):
    r=0

    for i in alist:
        r+=i**2
    return r

exec(input().strip())