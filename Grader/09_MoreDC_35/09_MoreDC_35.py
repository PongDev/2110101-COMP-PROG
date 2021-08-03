hsh={}
member={}
n=int(input())

for i in range(n):
    data=input().split()
    member[data[0]]=" ".join(data)
    for i in range(1,4):
        if data[i] not in hsh:
            hsh[data[i]]=set()
        hsh[data[i]].add(data[0])

query=input().split()
if query[0] in hsh:
    ans=set(hsh[query[0]])
    for i in query[1:]:
        if i in hsh:
            ans=ans.intersection(hsh[i])
        else:
            ans={}
            break
else:
    ans={}

if len(ans)==0:
    print("Not Found")
else:
    for data in sorted(ans):
        print(member[data])