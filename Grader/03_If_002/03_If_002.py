d,m,y = [int(e) for e in input().split()]
christYear=y-543

isLeap=False
if ((christYear%400==0) or (christYear%4==0 and christYear%100!=0)):
    isLeap=True

monthDayList=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if (isLeap):
    monthDayList[2]+=1

d+=15
if (d>monthDayList[m]):
    d-=monthDayList[m]
    m+=1
if (m>12):
    m=1
    y+=1
print(str(d)+"/"+str(m)+"/"+str(y))