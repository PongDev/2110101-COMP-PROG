mode=input()

if (mode=="str2RLE"):
    data=input()

    current=None
    count=0
    output=[]

    for i in data:
        if (i==current):
            count+=1
        else:
            if (current!=None):
                output.append(current)
                output.append(str(count))
            current=i
            count=1
    if (current!=None):
        output.append(current)
        output.append(str(count))

    print(" ".join(output))
    print()
elif (mode=="RLE2str"):
    data=input().split()

    for i in range(0,len(data),2):
        print(data[i]*int(data[i+1]),end="")
    print()
else:
    print("Error")