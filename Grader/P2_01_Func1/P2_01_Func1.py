def is_odd(n):
    return n%2==1

def has_odds(x):
    for i in x:
        if is_odd(i):
            return True
    return False

def all_odds(x):
    for i in x:
        if not is_odd(i):
            return False
    return True

def no_odds(x):
    return not has_odds(x)

def get_odds(x):
    r=[]

    for i in x:
        if is_odd(i):
            r.append(i)
    return r

def zip_odds(a,b):
    r=[]
    lst1=get_odds(a)
    lst2=get_odds(b)

    for i in range(max(len(lst1),len(lst2))):
        if (i<len(lst1)):
            r.append(lst1[i])
        if (i<len(lst2)):
            r.append(lst2[i])
    return r

exec(input().strip())