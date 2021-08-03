def spiral_square(n):
    data=[[0 for j in range(n)] for i in range(n)]
    i=j=n-1
    count=n*n
    mode=0 #0=left 1=up 2=right 3=down
    while count>0:
        data[i][j]=count
        count-=1
        if mode==0:
            if j-1<0 or data[i][j-1]!=0:i-=1;mode+=1
            else:j-=1
        elif mode==1:
            if i-1<0 or data[i-1][j]!=0:j+=1;mode+=1
            else:i-=1
        elif mode==2:
            if j+1==n or data[i][j+1]!=0:i+=1;mode+=1
            else:j+=1
        elif mode==3:
            if i+1==n or data[i+1][j]!=0:j-=1;mode+=1
            else:i+=1
        mode%=4
    return data

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())