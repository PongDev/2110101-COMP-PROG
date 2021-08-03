def read_matrix():
    m=[]
    nrows=int(input())
    for k in range(nrows):
        x=input().split()
        r=[]
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c,A):
    r=A

    for i in range(len(A)):
        for j in range(len(A[i])):
            r[i][j]*=c
    return r

def mult(A,B):
    r=[[0 for j in range(len(B[0]))] for i in range(len(A))]

    for i in range(len(r)):
        for j in range(len(r[i])):
            for k in range(len(A[0])):
                r[i][j]+=A[i][k]*B[k][j]
    return r

exec(input().strip())