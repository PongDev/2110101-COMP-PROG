n=int(input())
dataList=[]
dataDict={}
allVitData={}
avgVit=None
maxVit=None
for i in range(n):
    data=input().split()
    vitData=[float(e) for e in data[1:]]
    dataList.append(data)
    dataDict[data[0]]=data[1:]
    for key,value in enumerate(vitData):
        if key in allVitData:
            allVitData[key].append([value,data[0]])
        else:
            allVitData[key]=[[value,data[0]]]
    if avgVit==None:
        avgVit=vitData
    else:
        for key,value in enumerate(vitData):
            avgVit[key]+=value
    if maxVit==None:
        maxVit=[[e,data[0]] for e in vitData]
    else:
        for key,value in enumerate(vitData):
            if (value>maxVit[key][0]):
                maxVit[key]=[value,data[0]]
            elif (value==maxVit[key][0] and data[0]<maxVit[key][1]):
                maxVit[key][1]=data[0]
for i in range(len(vitData)):
    avgVit[i]/=n
cmd=input().split()
if (cmd[0]=="show"):
    for i in dataList:
        print(" ".join(i))
elif (cmd[0]=="get"):
    if cmd[1] in dataDict:
        print(cmd[1]," ".join(dataDict[cmd[1]]))
    else:
        print(cmd[1],"not found")
elif (cmd[0]=="avg"):
    print(round(avgVit[int(cmd[1])-1],4))
elif (cmd[0]=="max"):
    print(maxVit[int(cmd[1])-1][1],maxVit[int(cmd[1])-1][0])
elif (cmd[0]=="sort"):
    print(" ".join([e[1] for e in sorted(allVitData[int(cmd[1])-1])]))