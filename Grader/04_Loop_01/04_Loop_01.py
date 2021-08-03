sum=0
count=0
while True:
    data=input()
    if (data=="q"):
        break
    else:
        count+=1
        sum+=float(data)
if (count==0):
    print("No Data")
else:
    print(round(sum/count,2))