def read_next(f):
    while True:
        t=f.readline()
        if len(t)==0:
            break
        x=t.strip().split()
        if len(x)==2:
            return x[0],x[1]
    return "",""

def isLess(data1,data2):
    if data1=="":
        return False
    elif data2=="":
        return True
    elif int(data1[-2:])<int(data2[-2:]):
        return True
    elif int(data1[-2:])>int(data2[-2:]):
        return False
    else:
        if (int(data1[:-2])<int(data2[:-2])):
            return True
        else:
            return False

filenameList=input().split()
fp1=open(filenameList[0],"r")
fp2=open(filenameList[1],"r")

data1=read_next(fp1)
data2=read_next(fp2)
while True:
    if (data1==data2==("","")):
        break
    elif isLess(data1[0],data2[0]):
        print(data1[0],data1[1])
        data1=read_next(fp1)
    else:
        print(data2[0],data2[1])
        data2=read_next(fp2)

fp1.close()
fp2.close()