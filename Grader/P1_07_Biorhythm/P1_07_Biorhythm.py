import math

def isLeapYear(y):
    if (y%400==0 or (y%100!=0 and y%4==0)):
        return True
    else: return False

def dayOfYear(d,m,y):
    monthDay=[31,28,31,30,31,30,31,31,30,31,30,31]

    monthDay[1]+=(1 if isLeapYear(y) else 0)
    return sum(monthDay[:m-1])+d

def Biorhythm(day,n):
    return math.sin(2*math.pi*day/n)

bd,bm,by,d,m,y=[int(e) for e in input().split()]
# by+=1
# y+=1
by-=543
y-=543
dayCount=(365+(1 if isLeapYear(by) else 0)-dayOfYear(bd,bm,by)+1)+(365*(y-by-1))+dayOfYear(d,m,y)-1
print("{} {:.2f} {:.2f} {:.2f}".format(dayCount,Biorhythm(dayCount,23),Biorhythm(dayCount,28),Biorhythm(dayCount,33)))