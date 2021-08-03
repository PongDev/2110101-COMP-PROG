courseDict={}
teacherDict={}

courseFile=open(input(),"r")
for line in courseFile:
    line=line.strip().split(",")
    courseDict[line[0]]=line[1]
courseFile.close()

teacherFile=open(input(),"r")
for line in teacherFile:
    line=line.strip().split(",")
    teacherDict[line[0]]=line[1]
teacherFile.close()

dbFile=open(input(),"r")
for line in dbFile:
    line=line.strip().split(",")
    if line[0] in courseDict and line[1] in teacherDict:
        print(courseDict[line[0]]+","+teacherDict[line[1]])
    else:
        print("record error")
dbFile.close()