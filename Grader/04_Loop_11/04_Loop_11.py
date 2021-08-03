data=input()

last=data[0]
count=0
ans=""
for i in data:
    if (i==last):
        count+=1
    else:
        ans+=("" if ans=="" else " ")+last+" "+str(count)
        last=i
        count=1
ans+=("" if ans=="" else " ")+last+" "+str(count)
print(ans)