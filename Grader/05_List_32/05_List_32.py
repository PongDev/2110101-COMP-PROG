n = int(input())
newQ = 0
processQ = 0
DB = []
customerCount = 0
timeCount = 0
for query in range(n):
    mode = input().split()
    if (mode[0] == "reset"):
        newQ = processQ = int(mode[1])-1
    elif (mode[0] == "new"):
        newQ += 1
        DB.append([newQ, int(mode[1])])
        print("ticket", newQ)
    elif (mode[0] == "next"):
        processQ += 1
        print("call", processQ)
    elif (mode[0] == "order"):
        beginTime = 0
        endTime = int(mode[1])

        for i in DB:
            if i[0] == processQ:
                beginTime = i[1]
                DB.remove(i)
                break
        print("qtime", processQ, endTime-beginTime)
        customerCount += 1
        timeCount += endTime-beginTime
    elif (mode[0] == "avg_qtime"):
        print("avg_qtime", round(timeCount/customerCount, 4))
