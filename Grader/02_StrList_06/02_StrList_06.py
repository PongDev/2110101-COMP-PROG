data1=[0,0,0]
data2=[0,0,0]
data3=[0,0,0]
i=input().split(", ")
data1[0]=float(i[0][1:])
data1[1]=float(i[1])
data1[2]=float(i[2][:-1])
i=input().split(", ")
data2[0]=float(i[0][1:])
data2[1]=float(i[1])
data2[2]=float(i[2][:-1])
data3[0]=data1[0]+data2[0]
data3[1]=data1[1]+data2[1]
data3[2]=data1[2]+data2[2]
print(str(data1),"+",str(data2),"=",str(data3))