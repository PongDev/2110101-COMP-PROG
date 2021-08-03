data=input().split()

fp=open(data[0],"r")
data[1]=data[1][-2:]
dataCount=0
dataMin=100
dataMax=0
dataSum=0
for line in fp:
    line=line.split()
    if (line[0][:2]==data[1]):
        dataCount+=1
        score=float(line[1])
        dataSum+=score
        dataMin=min(dataMin,score)
        dataMax=max(dataMax,score)
if dataCount==0:
    print("No data")
else:
    print(dataMin,dataMax,dataSum/dataCount)
fp.close()