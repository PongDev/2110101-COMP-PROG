n=int(input())
m=int(input())
data=[]
for i in range(n):
    data.append([int(e) for e in input().split()])
isWin=[False,False,False]
isSpaceLeft=False
isError=False
for i in range(n):
    for j in range(n):
        if (data[i][j]==0):isSpaceLeft=True
        elif (1<=data[i][j]<=2):
            if (i+m-1<n):
                for k in range(m):
                    if (data[i+k][j]!=data[i][j]):break
                else:
                    isWin[data[i][j]]=True
            if (j+m-1<n):
                for k in range(m):
                    if (data[i][j+k]!=data[i][j]):break
                else:
                    isWin[data[i][j]]=True
            if (i+m-1<n) and (j+m-1<n):
                for k in range(m):
                    if (data[i+k][j+k]!=data[i][j]):break
                else:
                    isWin[data[i][j]]=True
            if (i-m+1>=0) and (j-m+1>=0):
                for k in range(m):
                    if (data[i-k][j-k]!=data[i][j]):break
                else:
                    isWin[data[i][j]]=True
        else:isError=True
if isError or (isWin[1] and isWin[2]):
    print("ERROR")
elif isWin[1]:
    print("1 WIN")
elif isWin[2]:
    print("2 WIN")
elif not isSpaceLeft:
    print("DRAW")
elif isSpaceLeft:
    print("NOT OVER")