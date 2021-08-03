n=int(input())
list1=list()
list2=list()
for i in range(n):
    data=input().split()
    if (i%2==0):
        list1.append(int(data[0]))
        list2.append(int(data[1]))
    else:
        list1.append(int(data[1]))
        list2.append(int(data[0]))
command=input()
if (command=="Zig-Zag"):
    print(min(list1),max(list2))
elif (command=="Zag-Zig"):
    print(min(list2),max(list1))