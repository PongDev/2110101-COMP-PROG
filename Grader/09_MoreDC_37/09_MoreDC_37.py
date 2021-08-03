n=int(input())
available={}

for i in range(n):
    key,value=input().split()
    available[key]=int(value)

dataList=[]

m=int(input())
for i in range(m):
    data=input().split()
    dataList.append([-float(data[1]),data[0],data[2:]])

ans=[]

dataList.sort()
for data in dataList:
    for subject in data[2]:
        if available[subject]>0:
            available[subject]-=1
            ans.append([data[1],subject])
            break

ans.sort()
for id,subject in ans:
    print(id,subject)