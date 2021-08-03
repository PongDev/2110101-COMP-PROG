data=input()

cardValue={
    "A":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
}
cardSet={
    "C":1,
    "D":2,
    "H":3,
    "S":4
}

r=""
for i in range(2,len(data),2):
    if (data[i]==data[i-2]):
        diffValue=cardSet[data[i-1]]-cardSet[data[i+1]]
    else:
        diffValue=cardValue[data[i-2]]-cardValue[data[i]]
    if (diffValue>0):
        r+="+"+str(diffValue)
    else:
        r+=str(diffValue)
print(r)