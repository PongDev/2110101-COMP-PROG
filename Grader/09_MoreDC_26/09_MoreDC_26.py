n=int(input())
memberList=[]
cityDict={}
memberDict={}

for i in range(n):
    data=input().split(": ")
    data[1]=data[1].split(", ")
    memberDict[data[0]]=data[1]
    memberList.append(data[0])
    for city in data[1]:
        if city not in cityDict:
            cityDict[city]=set()
        cityDict[city].add(data[0])

ansMember=set()
query=input()
for city in memberDict[query]:
    ansMember=ansMember.union(cityDict[city])
ansMember.remove(query)

if len(ansMember)==0:
    print("Not Found")
else:
    for i in memberList:
        if i in ansMember:
            print(i)