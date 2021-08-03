def calculateScore(doc,word):
    freq=doc["word_count"][word]/doc["all_word_count"] if word in doc["word_count"] else 0
    specific=1/len(doc["word_count"])
    return freq*specific

docList={}

n=int(input())

for i in range(n):
    docName=input()
    docData=input().split()
    docList[docName]={"all_word_count":len(docData),"word_count":{}}
    for word in docData:
        if word not in docList[docName]["word_count"]:
            docList[docName]["word_count"][word]=0
        docList[docName]["word_count"][word]+=1
while True:
    q=input()
    if q=="-1":
        break
    score=0
    targetDoc=""
    for doc in docList:
        docScore=calculateScore(docList[doc],q)
        if docScore>score:
            score=docScore
            targetDoc=doc
    if score==0:
        print("NOT FOUND")
    else:
        print(targetDoc)