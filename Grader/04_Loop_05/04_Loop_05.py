word=input()
rawSentence=input()

sentence=""
for i in rawSentence:
    if (i not in ["0","1","2","3","4","5","6","7","8","9","\"","(",")",",",".","'"]):
        sentence+=i
    else:
        sentence+=" "

sentence=sentence.split()
ans=0
for i in sentence:
    if (word==i):
        ans+=1
print(ans)