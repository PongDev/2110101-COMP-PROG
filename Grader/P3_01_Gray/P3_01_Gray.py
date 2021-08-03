def find(lv):
    if lv==1:
        return ["0","1"]
    else:
        r=find(lv-1)
        r=r+r[::-1]
        for i in range(len(r)):
            if i<len(r)//2:
                r[i]="0"+r[i]
            else:
                r[i]="1"+r[i]
        return r

n=int(input())
k=int(input())
if n<=0 and k<1:
    print("Invalid n and k")
elif n<=0:
    print("Invalid n")
elif k<1:
    print("Invalid k")
else:
    line=""
    for i in range(k):
        tmp=str(i+1)+("-"*n)
        line+=tmp[:n if i==k-1 else n+1]
    print(line)
    ans=find(n)
    for i in range(0,len(ans),k):
        print(",".join(ans[i:i+k]))