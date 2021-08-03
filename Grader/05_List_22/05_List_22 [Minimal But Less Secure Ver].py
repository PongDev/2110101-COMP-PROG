data = []

while True:
    i = input()
    if (i == "q"):
        break
    data.append(i.split())
data.sort()
GradeList = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
upGrade = input().split()
upGrade.sort()
processIdx = 0
for i in upGrade:
    while(data[processIdx][0] != i):
        processIdx += 1
    if (data[processIdx][1] != "A"):
        data[processIdx][1] = GradeList[GradeList.index(data[processIdx][1])-1]
for i in data:
    print(i[0], i[1])
