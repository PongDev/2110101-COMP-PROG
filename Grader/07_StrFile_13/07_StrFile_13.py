data=""
for i in input():
    if "A"<=i<="Z" or "a"<=i<="z" or "0"<=i<="9":
        data+=i
    else:
        data+=" "
data=data.split()
data[0]=data[0].lower()
for i in range(1,len(data)):
    data[i]=data[i][0].upper()+data[i][1:].lower()
data="".join(data)
print(data)