data=input().strip().lower()
n=int(input())
wordList=set()
for i in range(n):
    wordList.add(input().strip().lower())
output=""
noWordMode=False
ptr1=0
while ptr1<len(data):
    ptr2=-1
    for i in range(ptr1,len(data)):
        if (data[ptr1:i+1] in wordList):
            ptr2=i
    if ptr2==-1:
        if noWordMode:
            output+=data[ptr1]
        else:
            noWordMode=True
            output+=" "+data[ptr1]
    else:
        noWordMode=False
        output+=" "+data[ptr1:ptr2+1]
        ptr1=ptr2
    ptr1+=1
print(output.strip())