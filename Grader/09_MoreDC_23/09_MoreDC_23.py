n=int(input())

musicType={}
for i in range(n):
    data=input().split(", ")
    data[3]=[int (e) for e in data[3].split(":")]
    if data[2] not in musicType:
        musicType[data[2]]=0
    musicType[data[2]]+=(data[3][0]*60)+data[3][1]

lst=sorted([[value,key] for key,value in musicType.items()],reverse=True)

for value,key in lst[:3]:
    print(key,"-->",str(value//60)+":"+str(value%60).zfill(2))