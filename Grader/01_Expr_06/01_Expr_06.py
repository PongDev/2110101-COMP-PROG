startHour=int(input())
startMinute=int(input())
startSecond=int(input())
endHour=int(input())
endMinute=int(input())
endSecond=int(input())
resultHour=endHour-startHour
resultMinute=endMinute-startMinute
resultSecond=endSecond-startSecond

if (resultSecond<0):
    resultMinute-=1
    resultSecond+=60
if (resultMinute<0):
    resultHour-=1
    resultMinute+=60
if (resultHour<0):
    resultHour+=24
print(str(resultHour)+":"+str(resultMinute)+":"+str(resultSecond))