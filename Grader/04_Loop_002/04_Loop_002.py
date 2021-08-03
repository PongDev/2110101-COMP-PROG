data=[int(e) for e in input().split()]
p=data[-1]
i=-1
j=0
n=len(data)
while(j<n-1):
    if (data[j]<=p):
        i+=1
        data[i],data[j]=data[j],data[i]
    j+=1
data[i+1],data[-1]=data[-1],data[i+1]
print(data)