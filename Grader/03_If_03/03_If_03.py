data=input().split()
data[0]=float(data[0])
data[1]=float(data[1])
data[2]=float(data[2])
data[3]=float(data[3])
Sum=data[0]+data[1]+data[2]+data[3]
if (data[0]>=data[1] and data[0]>=data[2] and data[0]>=data[3]):
    Max=data[0]
if (data[1]>=data[0] and data[1]>=data[2] and data[1]>=data[3]):
    Max=data[1]
if (data[2]>=data[0] and data[2]>=data[1] and data[2]>=data[3]):
    Max=data[2]
if (data[3]>=data[0] and data[3]>=data[1] and data[3]>=data[2]):
    Max=data[3]

if (data[0]<=data[1] and data[0]<=data[2] and data[0]<=data[3]):
    Min=data[0]
if (data[1]<=data[0] and data[1]<=data[2] and data[1]<=data[3]):
    Min=data[1]
if (data[2]<=data[0] and data[2]<=data[1] and data[2]<=data[3]):
    Min=data[2]
if (data[3]<=data[0] and data[3]<=data[1] and data[3]<=data[2]):
    Min=data[3]

print(round((Sum-Max-Min)/2,2))