sumVoteByPoint={}
sumVoteByPerson={}
sumVoteByFavor={}
personalVote={}

while True:
    inputData=input().split()
    if len(inputData)==1:
        inputData[0]=int(inputData[0])
        if inputData[0]==1:
            ans=sorted([[-value,key] for key,value in sumVoteByPoint.items()])[:3]
        elif inputData[0]==2:
            for personName in personalVote:
                for idolData in personalVote[personName]:
                    if idolData not in sumVoteByPerson:
                        sumVoteByPerson[idolData]=0
                    sumVoteByPerson[idolData]+=1
            ans=sorted([[-value,key] for key,value in sumVoteByPerson.items()])[:3]
        elif inputData[0]==3:
            for personName in personalVote:
                mxVote=0
                idolName=""
                for key,value in personalVote[personName].items():
                    if value>mxVote:
                        mxVote=value
                        idolName=key
                    elif value==mxVote and key<idolName:
                        idolName=key
                if idolName not in sumVoteByFavor:
                    sumVoteByFavor[idolName]=0
                sumVoteByFavor[idolName]+=1
            ans=sorted([[-value,key] for key,value in sumVoteByFavor.items()])[:3]
        print(", ".join([e[1] for e in ans]))
        break
    voter,idol,score=inputData[0],inputData[1],int(inputData[2])
    if voter not in personalVote:
        personalVote[voter]={}
    if idol not in personalVote[voter]:
        personalVote[voter][idol]=score
    else:
        personalVote[voter][idol]+=score
    if idol not in sumVoteByPoint:
        sumVoteByPoint[idol]=0
    sumVoteByPoint[idol]+=score