import math

data=input().split(",")
originalLen=[len(data[0]),len(data[1]),len(data[2])]
data[0]=int(data[0])
data[1]=float("0."+data[1])
data[2]=float("0."+("0"*originalLen[1])+data[2])
beforeDuplicate=float(data[0]+data[1])
afterDuplicate=beforeDuplicate+data[2]
noneDuplicateDigit=originalLen[1]
duplicateDigit=originalLen[2]
Upper=(((10**duplicateDigit)*afterDuplicate)-beforeDuplicate)
Lower=(10**duplicateDigit)-1
Upper*=10**noneDuplicateDigit
Lower*=10**noneDuplicateDigit
Upper=int(Upper)
Lower=int(Lower)
gcd=math.gcd(Upper,Lower)
Upper//=gcd
Lower//=gcd
print(str(Upper)+" / "+str(Lower))