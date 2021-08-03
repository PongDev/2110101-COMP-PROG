def pattern1(nrows,ncols):
    return [[(i*ncols)+(j+1) for j in range(ncols)] for i in range(nrows)]

def pattern2(nrows,ncols):
    return [[(i+1)+(j*nrows) for j in range(ncols)] for i in range(nrows)]

def pattern3(N):
    r=[[0 for j in range(N)] for i in range(N)]

    count=1
    for i in range(N):
        for j in range(N-i):
            r[i][j+i]=count
            count+=1
    return r

def pattern4(N):
    r=[[0 for i in range(N)] for i in range(N)]

    count=1
    for i in range(N):
        for j in range(i,-1,-1):
            r[j][i]=count
            count+=1
    return r


def pattern5(N):
    r=[[0 for j in range(N)] for i in range(N)]

    count=1
    for i in range(N):
        for j in range(N-i):
            r[j][j+i]=count
            count+=1
    return r

def pattern6(N):
    r=[[0 for j in range(N)] for i in range(N)]

    count=1
    for i in range(N):
        for j in (range(N-i) if i%2==0 else range(N-i-1,-1,-1)):
            r[j][j+i]=count
            count+=1
    return r

exec(input().strip())