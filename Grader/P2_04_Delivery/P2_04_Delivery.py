def verifyDate(date):
    dayInMonth=[0,31,28,31,30,31,30,31,31,30,31,30,31]

    christYear=date[2]-543
    if (christYear%400==0) or (christYear%4==0 and christYear%100!=0):
        dayInMonth[2]+=1
    return True if (1<=date[0]<=dayInMonth[date[1]]) else False

def verifyData(data):
    if data[4]<2558:
        return "Invalid year"
    elif (data[3]<1 or data[3]>12):
        return "Invalid month"
    elif verifyDate(data[2:])==False:
        return "Invalid date"
    elif data[1] not in ["E","Q","N","F"]:
        return "Invalid delivery type"
    return None

def getDate(data):
    deliveryTime={
        "E":1,
        "Q":3,
        "N":7,
        "F":14
    }
    dayInMonth=[0,31,28,31,30,31,30,31,31,30,31,30,31]

    date=data[2:]
    christYear=date[2]-543
    if (christYear%400==0) or (christYear%4==0 and christYear%100!=0):
        dayInMonth[2]+=1
    date[0]+=deliveryTime[data[1]]
    if (date[0]>dayInMonth[date[1]]):
        date[0]%=dayInMonth[date[1]]
        date[1]+=1
    if (date[1]>12):
        date[1]%=12
        date[2]+=1

    date.reverse()
    return date

errorData=[]
deliveryData=[]

while True:
    rawData=input().strip()
    if (rawData=="END"):
        for i in errorData:
            print(i)
        for i in sorted(deliveryData):
            print(str(i[1])+": delivered on "+str(i[0][2])+"/"+str(i[0][1])+"/"+str(i[0][0]))
        break
    processData=[int(e) if key>1 else e for key,e in enumerate(rawData.split())]
    error=verifyData(processData)
    if error!=None:
        errorData.append("Error: "+rawData+" --> "+error)
    else:
        deliveryData.append([getDate(processData),processData[0]])