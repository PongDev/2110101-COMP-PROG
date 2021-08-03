filename=input()
mode=input()

if mode not in ["LSTRIP","RSTRIP","STRIP","STRIP_ALL"]:
    print("Invalid command")
else:
    data=[]
    fp=open(filename,"r")
    for line in fp:
        data.append(line.strip())
    fp.close()
    def checkDotColumn(col):
        for row in data:
            if row[col]!=".":return False
        else:return True
    if mode=="STRIP_ALL":
        dotColumn=set()
        for i in range(len(data[0])):
            if checkDotColumn(i):
                dotColumn.add(i)
        for row in data:
            for i in range(len(row)):
                if i not in dotColumn:
                    print(row[i],end="")
            print()
    else:
        lpos=0
        rpos=0
        for i in range(len(data[0])):
            if not checkDotColumn(i):
                lpos=i
                break
        for i in range(len(data[0]))[::-1]:
            if not checkDotColumn(i):
                rpos=i+1
                break
        if mode=="LSTRIP":rpos=len(data[0])
        elif mode=="RSTRIP":lpos=0
        for row in data:
            print(row[lpos:rpos])