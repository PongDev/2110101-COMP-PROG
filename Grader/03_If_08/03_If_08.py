day=int(input())
month=int(input())
year=int(input())
year-=543

if ((year%400==0) or (year%100!=0 and year%4==0)):
    isLeapYear=True
else:
    isLeapYear=False

if (month>1):
    day+=31
if (month>2):
    day+=28
    if (isLeapYear):
        day+=1
if (month>3):
    day+=31
if (month>4):
    day+=30
if (month>5):
    day+=31
if (month>6):
    day+=30
if (month>7):
    day+=31
if (month>8):
    day+=31
if (month>9):
    day+=30
if (month>10):
    day+=31
if (month>11):
    day+=30
if (month>12):
    day+=31
print(day)