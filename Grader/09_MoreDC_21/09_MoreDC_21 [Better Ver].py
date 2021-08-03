def factor(N):
    r=[]

    p=2
    while(N>1):
        time=0
        while N%p==0:
            N//=p
            time+=1
        if time!=0:
            r.append([p,time])
        p+=1
    return r

exec(input().strip())