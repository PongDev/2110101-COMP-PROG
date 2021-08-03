data=input().lower()
hsh={}
for i in data:
    if "a"<=i<="z":
        if i in hsh:
            hsh[i]+=1
        else:
            hsh[i]=1
lst=sorted([[-hsh[key],key] for key in hsh])
for count,key in lst:
    print(key,"->",-count)