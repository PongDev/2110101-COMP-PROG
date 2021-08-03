def getScore(idx):
    if (idx>=len(data)):
        return 0
    elif (data[idx]=="X"):
        return 10
    elif (data[idx]=="/"):
        return 10-int(data[idx-1])
    else:
        return int(data[idx])

data=input()
command=int(input())

score=[]

i=0
while i<len(data) and len(score)<10:
    if (data[i]=="X"):
        score.append(getScore(i)+getScore(i+1)+getScore(i+2))
    else:
        score.append(getScore(i)+getScore(i+1))
        if (data[i+1]=="/"):
            score[len(score)-1]+=getScore(i+2)
        i+=1
    i+=1

print (score[command-1] if (1<=command<=10) else sum(score))