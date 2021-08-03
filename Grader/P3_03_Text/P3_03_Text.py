filename=input().strip()
k=int(input())

fp=open(filename,"r")
data=fp.read().replace("\n",".")
fp.close()
tmp=""
dotCount=0
processData=[]
for i in data:
    if i==".":
        if tmp!="":
            processData.append(tmp)
            tmp=""
        dotCount+=1
    else:
        if dotCount>0:
            processData.append(dotCount)
            dotCount=0
        tmp+=i
processData.append(tmp)
ruler=''
for i in range(k//10):
    ruler+='-'*9+str(i+1)
ruler+='-'*(k%10)
print(ruler)
pos=0
left=k
while pos<len(processData):
    if (type(processData[pos])==str):
        if (left>=len(processData[pos])):
            left-=len(processData[pos])
            print(processData[pos],end="")
        elif left==k and len(processData[pos])>k:
            print(processData[pos],end="")
            left=0
        if left<=0:
            left=k
            print()
    elif (type(processData[pos])==int):
        if left==k:
            pass
        elif left>=processData[pos]+len(processData[pos+1]):
            print("."*processData[pos],end="")
            left-=processData[pos]
        else:
            left=k
            print()
    pos+=1