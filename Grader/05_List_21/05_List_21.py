id = []
grade = []

while True:
    i = input().split()
    if (i[0] == "q"):
        break
    id.append(i[0])
    grade.append(i[1])

GradeList = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
upGrade = input().split()
for i in upGrade:
    targetPos = id.index(i)
    if (grade[targetPos] != "A"):
        grade[targetPos] = GradeList[GradeList.index(grade[targetPos])-1]

for i in range(len(id)):
    print(id[i], grade[i])
