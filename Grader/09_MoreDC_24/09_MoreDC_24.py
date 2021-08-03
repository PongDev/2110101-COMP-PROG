animalDict={}
animalOrder=[]

while True:
    data=input().split(", ")
    if data[0]=="q":break
    if data[1] not in animalDict:
        animalOrder.append(data[1])
        animalDict[data[1]]=[]
    animalDict[data[1]].append(data[0])

for animal in animalOrder:
    print(animal+":",", ".join(animalDict[animal]))