data = []
validID = []

while True:
    i = input().split()
    if (i[0] == "q"):
        break
    data.append([int(i[0]), i[1]])
    validID.append(int(i[0]))
data.sort()
GradeList = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
upGrade = input().split()
upGrade.sort()
processIdx = 0
for i in upGrade:
    i = int(i)
    if i in validID:
        while(data[processIdx][0] != i):
            processIdx += 1
        if (data[processIdx][1] != "A"):
            data[processIdx][1] = GradeList[GradeList.index(data[processIdx][1])-1]
for i in data:
    print(i[0], i[1])
